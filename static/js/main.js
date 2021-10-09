(function(){
    // pub and sub
    (function(){
        var o = $({});
        $.subscribe = function() {
            o.on.apply(o, arguments);
        };
        $.unsubscribe = function() {
            o.off.apply(o, arguments);
        };
        $.publish = function() {
            o.trigger.apply(o, arguments);
        };
    })();
    var hasTouch = (typeof(window.ontouchstart) !== 'undefined'&&window.ontouchstart);
    var eventType = 'click';
    if (hasTouch) {
        eventType = 'touchstart';
    }
    var center = {};
    center.Hash = (function() {
        var fromHash = function() {
            var params = [];
            var paramsObject = {};
            var hash = window.location.hash;
            if(hash){
                hash = hash.split('?')[0];
                params = hash.substr(1).split("&");
            }

            for (var i = 0; i < params.length; i++) {
                var a = params[i].split("=");
                paramsObject[a[0]] = decodeURIComponent(a[1]);
            }
            return paramsObject;
        };
        var toHash = function(params) {
            var str = [];
            for (var p in params) {
                str.push(p + "=" + encodeURIComponent(params[p]));
            }
            window.location.hash = str.join("&");
        };
        return {
            get: function(param) {
                var params = fromHash();
                if (param) {
                    return params[param];
                } else {
                    return params;
                }
            },
            add: function(newParams) {
                var params = fromHash();
                for (var p in newParams) {
                    params[p] = newParams[p];
                }
                toHash(params);
            },
            remove: function(removeParams) {
                removeParams = (typeof(removeParams) == 'string') ? [removeParams] : removeParams;
                var params = fromHash();
                for (var i = 0; i < removeParams.length; i++) {
                    delete params[removeParams[i]];
                }
                toHash(params);
            },
            clear: function() {
                toHash({});
            }
        };
    })();
    center.getNodes = function(wrap,attr) {
        var attr = attr||'node-type';
        var nodes = $("[" + attr + "]", wrap);
        var nodesObj = {};
        nodesObj.wrap = wrap;
        nodes.each(function(i) {
            var item = $(this);
            nodesObj[item.attr(attr)] = item;
        });
        return nodesObj;
    };
    // 评论提醒
    center.SideCmntTip = (function(){
        var wrap = null;
        var tip = null;
        return {
            toggle:function(num){
                var max = 99;
                if(!wrap){
                    wrap = $('#SI_SideTab [node-relation=cmnt]');
                }
                if(!tip){
                    tip = $('<span class="l_menu_tip" style="display:none;"></span>').appendTo(wrap);
                }
                // num = 100; 测试
                if(num===0){
                    tip.hide();
                }else{
                    if(num>max){
                        num ='<em>'+max+'<sup>+</sup></em>';
                    }
                    tip.html(num).show();
                }
            }
        };
    })();
    // 选项卡
    center.Tab = (function(){
        var Tab = function(id,clz){
            var self = this;
            self.wrap = null;
            self.dom = null;
            self.currentClz = '';
            self.id = '';
            self.init(id,clz);
        };
        Tab.prototype = {
            init:function(id,clz){
                var self = this;
                self.wrap = $('#'+id);
                self.id = id;
                self.currentClz = clz;
                self.dom = center.getNodes(self.wrap,'node-relation');
                this.bind();
            },
            show:function(type){
                var self = this;
                var current = self.dom[type];
                if(!current){
                    return;
                }
                if (current.hasClass('.'+ self.currentClz)) {
                    return;
                }
                self.wrap.find('.'+ self.currentClz)
                    .removeClass(self.currentClz);
                current.addClass(self.currentClz);
                $.publish(self.id, type);
            },
            bind:function(){
                var self = this;
                self.wrap.on(eventType,'[node-relation]',function(e){
                    e.stopPropagation();
                    var current = $(this);
                    var type = current.attr('node-relation');
                    self.show(type);
                });
            }
        };

        return Tab;

    })();
    // 评论列表（回复我的+我评论的）
    center.CmntList = (function(){
        var ReachBottom = (function(){
          var addEvent = function(el, type, fn, captrue) {
            if (typeof captrue == 'undefined') {
              captrue = false;
            }
            if (el.addEventListener) {
              el.addEventListener(type, fn, captrue);
              return true;
            } else if (el.attachEvent) {
              el.attachEvent('on' + type, fn);
              return true;
            } else {
              el['on' + type] = fn;
            }
          };
          var throttle = function(fn, delay){
              var timer = null;
              return function(){
                  var context = this, args = arguments;
                  clearTimeout(timer);
                  timer = setTimeout(function(){
                      fn.apply(context, args);
                  }, delay);
              };
           };
          var toBottom = (function() {
            var docEle = document.documentElement;
            var docBody = document.body;
            var _min = Math.min;
            var _max = Math.max;
            return function() {
              var scrollTop = 0;
              var clientHeight = 0;
              var scrollHeight = 0;
              try {
                if (docEle && docEle.scrollTop) {
                  scrollTop = docEle.scrollTop;
                } else if (docBody) {
                  scrollTop = docBody.scrollTop;
                }
                if (docBody.clientHeight && docEle.clientHeight) {
                  clientHeight = _min(docBody.clientHeight, docEle.clientHeight)
                } else {
                  clientHeight = _max(docBody.clientHeight, docEle.clientHeight);
                }
                scrollHeight = _max(docBody.scrollHeight, docEle.scrollHeight);
                return (scrollHeight - scrollTop - clientHeight);
              } catch (e) {
                return false;
              }
            };
          })();
          var fns = [];
          var inited = false;
          return function(fn){
            fns.push(fn);
            if(!inited){
              var thottle1 = throttle(function(){
                for (var i = 0, len = fns.length; i < len; i++) {
                  var fn = fns[i];
                  if(typeof fn === 'function'){
                    fn(toBottom());
                  }
                }
              },100);
              addEvent(window, 'scroll', function() {
                thottle1();
              });
            }
          };
        })();
        var List = function(wrap,url,uid,type,loaded){
            var self = this;
            self.wrap = $('#'+wrap);
            self.pause = true;
            self.uid = uid;
            self.url = url+'?uid='+uid;
            self.type = type;
            self.loaded = loaded;
        };
        List.prototype = {
            init:function(){
                var self = this;
                // if(!self.List){
                    ___mysInacMNT___.cmnt.config.encoding = 'utf-8';
                    self.List = new ___mysInacMNT___.cmnt.List(self.wrap[0],self.url, {
                        type: self.type,
                        uid:self.uid,
                        page: 1,
                        pageSize: 20,
                        loaded:function(listSelf){
                            if(typeof self.loaded === 'function'){
                                self.loaded(listSelf);
                            }
                        }
                      });
                    self.bind();
                // }
                self.pause = false;
            },
            bind:function(){
                var self = this;
                var getPage = function(list){
                   return list.get('opt.param.page')
                };
                ReachBottom(function(gap){

                  if(gap<50){
                    // 如果还有数据 并且没有暂停滚动 则继续
                    if(self.hasData() && !self.pause){
                      var page = getPage(self.List);
                      page++;
                      self.List.setPage(page).getData(function(){

                      });
                    }
                  }
                });
            },
            hasData:function(){
                var self = this;
                var List = self.List;
                if(List.data && List.data.cmntlist && List.data.cmntlist.length>0){
                    return true;
                }else{
                    return false;
                }
            },
            scrollPause:function(flag){
                var self = this;
                self.pause = flag;
            }
        };
        return List;
    })();
    center.isLogin = function(fn){
        var isLogin = false;
        if(SINA_OUTLOGIN_LAYER&&SINA_OUTLOGIN_LAYER.isLogin()){
            isLogin = true;
        }
        if(typeof fn === 'function'){
            fn(isLogin);
        }
        return isLogin;
    };
    center.getUid = function(){
        var uid = '';
        var userCookie = SINA_OUTLOGIN_LAYER.getSinaCookie();
        if(userCookie){
            uid = userCookie.uid;
        }
        return uid;
    };
    center.uidIsChanged = function(configUid,fn){
        var isChanged = (configUid=== center.getUid());

        if(typeof fn === 'function'){
            fn(isChanged);
        }
        return isChanged;
    };

    window.__CENTER__ = center;
})();

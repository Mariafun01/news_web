/*
 字符串助手类
 作者:蓝色思维
 创建日期：2021-6-7
 */
const stringHelper={
    /**
     *从请求网址中获取查询参数值
     * 示例:
     * var html='demo4.html?id=1001&name=小红';
     * var name=stringHelper.requet_parameter(html,"name")
     * //那么返回 "小红"
     *
     * @param url 请求的网址
     * @param key 查询参数名
     * @return 参数的值
     */
    requet_parameter:function (url,key){
        if(url.indexOf("?")==-1){
            return null;
        }
        var arr=url.split('?')
        part=arr[1].split("&")
        result=null;
        for (const item of part) {
            part2=item.split('=');
            if(part2[0]==key){
                result=part2[1]
            }
        }
        return result;
    },
}





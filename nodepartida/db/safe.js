var safe=function()
{
	this.escape_mysql=function(obj)
	{
		try
		{
			var paramsindex=Object.keys(obj);
			for(var i in paramsindex)
			{
				if(typeof obj[paramsindex[i]]==="string")
					obj[paramsindex[i]]=this.escapeString(obj[paramsindex[i]]);
			}
			return obj;
		}catch(err)
		{
			if(typeof obj==="string")
				obj=this.escapeString(obj);
			return obj;
		}
		
	}
	this.escapeString=function(str) {

    return str.replace(/[\0\x08\x09\x1a\n\r"'\\\%]/g, function (char) {
        switch (char) {
            case "\0":
                return "\\0";
            case "\x08":
                return "\\b";
            case "\x09":
                return "\\t";
            case "\x1a":
                return "\\z";
            case "\n":
                return "\\n";
            case "\r":
                return "\\r";
            case "\"":
            case "'":
            	return "''";
            case "\\":
            case "%":
                return "\\"+char;
        	}
    	});
	}
	return this;
}
module.exports=safe;
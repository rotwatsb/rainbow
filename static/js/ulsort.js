function sortComments(ul) {
    var new_ul = ul.cloneNode(false);
    var lis = [];
    var all_divs = [];
    var top_divs = [];
    for(var i = ul.childNodes.length; i--;) {
	var lichild = ul.childNodes[i];
        if (lichild.nodeName === 'LI') {
            lis.push(lichild);
	    for(var j = lichild.childNodes.length; j--;) {
		var divchild = lichild.childNodes[j];
		if (divchild.nodeName === 'DIV') {
		    all_divs.push(divchild);
		    if (divchild.getAttribute('data-comment-level' == "0"))
			top_divs.push(divchild);
		    console.log(divchild.nodeName);
		    console.log(divchild.nodeType);
		    console.log(divchild.getAttribute('data-comment-level'));
		}
	    }
	}
    }
    
    addChil
    for(var i = divs.length; i--;) {
	
    }
    //lis.sort(function(a, b) {
    //    return parseInt(b.childNodes[0].data , 10) - parseInt(a.childNodes[0].data , 10);
    //});
    for(var i = 0; i < lis.length; i++)
        new_ul.appendChild(lis[i]);
    ul.parentNode.replaceChild(new_ul, ul);
}

function addChildren(divs, children) {

}

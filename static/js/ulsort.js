function sortComments(li) {
    var new_li = li.cloneNode(false);
    var nest_divs = [];
    var top_divs = [];
 /*
    for(var i = li.childNodes.length; i--;) {
	console.log(li.childNodes[i].nodeType);
	if (li.childNodes[i].nodeName === 'DIV') {
	    if (li.childNodes[i].getAttribute('data-comment-level' == "0"))
		top_divs.push(li.childNodes[i]);
	    else
		nest_divs.push(li.childNodes[i]);
	}
    }
    //console.log(top_divs.length);
    for (var div in top_divs) {
	console.log(div.nodeName);
	console.log(div.nodeType);
	console.log(div.getAttribute('data-comment-level'));

	addChildren(div, nest_divs);
	new_li.appendChild(div);
    }

    
    //lis.sort(function(a, b) {
    //    return parseInt(b.childNodes[0].data , 10) - parseInt(a.childNodes[0].data , 10);
    //});

    li.parentNode.replaceChild(new_li, li);
*/
}

function addChildren(par_div, lost_divs) {
    var still_lost_divs = [];
    var found_divs = [];
    for(var div in lost_divs) {
	if (div.getAttribute('data-comment-parentid') ==
	    par_div.getAttribute('data-comment-id')) {
	    par_div.appendChild(div);
	    found_divs.push(div);
	}
	else
	    still_lost_divs.push(div);
    }
    for (div in found_divs)
	addChildren(div, still_lost_divs);
}

function sortComments(ul) {
    var new_ul = ul.cloneNode(false);
    var nest_lis = [];
    var top_lis = [];

    for (var i = 0; i < ul.childNodes.length; i++) {
	if (ul.childNodes[i].nodeName === 'LI') {
	    if (ul.childNodes[i].getAttribute('data-comment-level') == "0")
		top_lis.push(ul.childNodes[i]);
	    else
		nest_lis.push(ul.childNodes[i]);
	}
    }

    for (var i = 0; i < top_lis.length; i++) {
	addChildren(new_ul, top_lis[i], nest_lis);
	new_ul.appendChild(top_lis[i]);
    }

    ul.parentNode.replaceChild(new_ul, ul);
}

function addChildren(ul, top_li, lost_lis) {
    var new_ul = ul.cloneNode(false);
    var new_kids = []
    var still_lost = [];
    var hasChild = false;
    for(var i = 0; i < lost_lis.length; i++) {
	if (lost_lis[i].getAttribute('data-comment-parentid') ==
	    top_li.getAttribute('data-comment-id')) {
	    new_ul.appendChild(lost_lis[i]);
	    new_kids.push(lost_lis[i]);
	    hasChild = true;
	}
	else
	    still_lost.push(lost_lis[i]);
    }
    for (var i = 0; i < new_kids.length; i++)
	addChildren(new_ul, new_kids[i], still_lost);
    
    if (hasChild)
	top_li.appendChild(new_ul);
}

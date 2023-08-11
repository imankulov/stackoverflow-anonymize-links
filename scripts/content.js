/*
 * Remove the user id from the end of the URL.
 */
document.querySelectorAll("a[data-controller='se-share-sheet']").forEach(function(element) {
    element.href = element.href.replace(/\d+$/, "").replace(/\/$/, "");
    element.setAttribute("data-se-share-sheet-subtitle", "(Without your user id)");
});
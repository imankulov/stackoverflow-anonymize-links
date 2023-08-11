/*
 * Remove the user id from the end of the URL.
 */
document.querySelectorAll("a[data-controller*='se-share-sheet']").forEach(function(element) {
    // First, see if the link matches the pattern q/12345/12345 or a/12345/12345.
    // If not then we don't need to do anything.
    if (!element.href.match(/\/(q|a)\/\d+\/\d+\/?$/)) {
        return;
    }
    // Delete user ID from the link
    element.href = element.href.replace(/\/\d+$/, "")
    // Delete a warning about the user ID
    element.removeAttribute("data-se-share-sheet-subtitle");
});
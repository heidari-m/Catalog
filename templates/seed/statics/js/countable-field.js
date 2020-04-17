(function() {
    function CountableField(textarea) {
        var countDisplay = document.getElementById(textarea.id + "_counter");
        var countDown = false;
        var minCount, maxCount;
        if (textarea != null && countDisplay != null) {
            minCount = textarea.getAttribute("data-min-count");
            maxCount = textarea.getAttribute("data-max-count");

            Countable.on(textarea, updateFieldWordCount);
        }

        function updateFieldWordCount(counter) {
            var count = counter["words"];
            countDisplay.getElementsByClassName("text-count-current")[0].innerHTML = count;
            if (minCount && count  maxCount)
                countDisplay.className = "text-count text-is-over-max";
            else
                countDisplay.className = "text-count";
        }
    }

    document.addEventListener('DOMContentLoaded', function(e) {
        ;[].forEach.call(document.querySelectorAll('[data-count]'), CountableField)
    })
})()
document.addEventListener("DOMContentLoaded", function () {
    function updateTime() {
        const timeElement = document.getElementById("current-time");
        const now = new Date();

        // Format time as HH:MM:SS
        const formattedTime = now.toLocaleTimeString();

        if (timeElement) {
            timeElement.textContent = "Current Time: " + formattedTime;
        }
    }

    // Update time immediately and then every second
    updateTime();
    setInterval(updateTime, 1000);
});
document.addEventListener("DOMContentLoaded", function () {
    function updateTime() {
        const timeElement = document.getElementById("current-time");
        const now = new Date();

        // Format time as HH:MM:SS
        const formattedTime = now.toLocaleTimeString();

        if (timeElement) {
            timeElement.textContent = "Time: " + formattedTime;
        }
    }

    // Update time immediately and then every second
    updateTime();
    setInterval(updateTime, 1000);
});
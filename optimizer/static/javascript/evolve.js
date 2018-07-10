var source = new EventSource("/evolve");
source.onmessage = function(event) {
    $('.progress-bar').css('width', event.data+'%').attr('aria-valuenow', event.data);
    $('.progress-bar-label').text(event.data+'%');

    if(event.data == 100){
        source.close();
        alert("Finished running! Moving you along now");
        //window.location.replace("http://stackoverflow.com");
	    document.location.href = '/results'
    }
}
//window.location.replace("http://stackoverflow.com");

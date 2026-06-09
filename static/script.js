function refreshGraphs() {

    let signalGraph =
        document.getElementById("signalGraph");

    let fftGraph =
        document.getElementById("fftGraph");

    signalGraph.src =
        "/static/graphs/signal_graph.png?t="
        + new Date().getTime();

    fftGraph.src =
        "/static/graphs/fft_graph.png?t="
        + new Date().getTime();
}

setInterval(refreshGraphs, 3000);
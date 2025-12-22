async function iniciar() {
  try {
    await fetch("https://deliverymoto-flask.onrender.com");
  } catch (e) {
    console.log("Backend ainda acordando...");
  } finally {
    document.getElementById("loading").style.display = "none";
    document.getElementById("app").style.display = "block";
  }
}

iniciar();

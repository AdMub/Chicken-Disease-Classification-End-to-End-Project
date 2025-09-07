let base_data = "";

document.getElementById("fileinput").addEventListener("change", function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement("img");
            img.src = e.target.result;
            document.getElementById("preview").innerHTML = "";
            document.getElementById("preview").appendChild(img);

            // Convert to base64 without prefix
            const image = new Image();
            image.src = e.target.result;
            image.onload = function() {
                const canvas = document.createElement("canvas");
                const ctx = canvas.getContext("2d");
                canvas.width = image.width;
                canvas.height = image.height;
                ctx.drawImage(image, 0, 0);
                base_data = canvas.toDataURL("image/jpeg").replace(/^data:image\/jpeg;base64,/, "");
            };
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById("send").addEventListener("click", function() {
    if (!base_data) {
        alert("Please upload an image first!");
        return;
    }

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ image: base_data })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = 
            `<h3>Prediction: ${data[0].image}</h3>`;
    })
    .catch(err => console.error(err));
});

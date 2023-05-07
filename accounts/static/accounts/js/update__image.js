const profileImageInput = document.getElementById("profile_image");
const profileImagePreview = document.getElementById("preview");

if (profileImageInput) {
    profileImageInput.addEventListener("change", function () {
        const file = this.files[0];
        const reader = new FileReader();
        reader.addEventListener("load", function () {
            profileImagePreview.src = reader.result;
            profileImagePreview.style.display = "block";
        });
        reader.readAsDataURL(file);
    });
}  
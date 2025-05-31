console.log("Swiper loaded");

var swiper = new Swiper(".mySwiper", {
  loop: false, // Optional: remove infinite loop if not needed
  grabCursor: true,
  spaceBetween: 20,
  slidesPerView: 2, // Shows 2 cards at a time
  centeredSlides: false,
  autoplay: false, // Disable autoplay
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: false, // Disable prev/next arrows
});

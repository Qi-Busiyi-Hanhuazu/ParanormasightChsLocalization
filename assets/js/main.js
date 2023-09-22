$(() => {
  /* 轮播设置 */
  setTimeout(() => {
    let items = $(".para-carousel .carousel-item");
    let items_length = items.length;
    let load_image = (event) => {
      let left = (event.to - 1 + items_length) % items_length;
      let right = (event.to + 1) % items_length;
      for (item_index of [left, right]) {
        let item = items[item_index];
        $(item).find("img").removeAttr("loading");
      }
    };
    $(".para-carousel").on("slide.bs.carousel", load_image);
    load_image({ to: 0 });
  }, 0);

  /* Han.js */
  setTimeout(() => {
    Han(document.body).render();
  }, 0);
});

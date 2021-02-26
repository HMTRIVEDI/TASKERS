const callback = function(entries) {
  entries.forEach(entry => {
    entry.target.classList.toggle(".jello-horizontal");
  });
};

const observer = new IntersectionObserver(callback);

const targets = document.querySelectorAll(".show-on-scroll");
targets.forEach(function(target) {
  observer.observe(target);
});
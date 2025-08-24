AFRAME.registerComponent('hover-animation', {
  init: function () {
    const el = this.el;

    // Add raycaster to make the entity interactive
    el.setAttribute('class', 'interactive');

    el.addEventListener('mouseenter', function () {
      // Pause the animation when cursor hovers over the model
      if (el.components.animation) {
        el.components.animation.pause();
      }
    });

    el.addEventListener('mouseleave', function () {
      // Resume the animation when cursor leaves the model
      if (el.components.animation) {
        el.components.animation.play();
      }
    });
  }
});

// Wait for the scene to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
  const scene = document.querySelector('a-scene');

  if (scene.hasLoaded) {
    setupInteractions();
  } else {
    scene.addEventListener('loaded', setupInteractions);
  }

  function setupInteractions() {
    // Add the hover-animation component to all animated models
    const models = document.querySelectorAll('a-gltf-model[animation]');

    models.forEach(model => {
      model.setAttribute('hover-animation', '');
    });

    // Update the cursor to only interact with elements that have the 'interactive' class
    const cursor = document.querySelector('a-cursor');
    if (cursor) {
      cursor.setAttribute('raycaster', 'objects: .interactive');
    }
  }
});

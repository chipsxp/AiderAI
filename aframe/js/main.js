// Main JavaScript file for A-Frame interactions

document.addEventListener('DOMContentLoaded', function() {
  console.log('A-Frame VR Experience loaded');
  
  // Register a component for interactive objects
  AFRAME.registerComponent('interactive', {
    init: function() {
      let el = this.el;
      
      // Change color on hover
      el.addEventListener('mouseenter', function() {
        this.setAttribute('color', '#FFFF00');
      });
      
      el.addEventListener('mouseleave', function() {
        // Restore original color based on shape
        if (this.tagName === 'A-BOX') {
          this.setAttribute('color', '#4CC3D9');
        } else if (this.tagName === 'A-SPHERE') {
          this.setAttribute('color', '#EF2D5E');
        } else if (this.tagName === 'A-CYLINDER') {
          this.setAttribute('color', '#FFC65D');
        }
      });
      
      // Add animation on click
      el.addEventListener('click', function() {
        // Create a random animation
        const animations = [
          {property: 'rotation', to: '0 360 0', dur: 2000},
          {property: 'position', to: this.getAttribute('position').x + ' ' + 
                                     (parseFloat(this.getAttribute('position').y) + 1) + ' ' + 
                                     this.getAttribute('position').z, dur: 1000, dir: 'alternate', loop: 2}
        ];
        
        const randomAnim = animations[Math.floor(Math.random() * animations.length)];
        
        this.setAttribute('animation', randomAnim);
      });
    }
  });
  
  // Add the interactive component to all elements with class "interactive"
  const scene = document.querySelector('a-scene');
  scene.addEventListener('loaded', function() {
    const interactiveEls = document.querySelectorAll('.interactive');
    interactiveEls.forEach(function(el) {
      el.setAttribute('interactive', '');
    });
  });
});

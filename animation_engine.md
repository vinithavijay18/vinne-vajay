# 🪄 The Pure Animation Engine

If you want to use these effects in other projects, here are the specific CSS keyframes and the JavaScript logic that controls them.

### **1. The CSS (The Visual Physics)**

This handles the "Heartbeat" pulse for the button and the "Swirling" physics for the emojis.

```css
/* -- THE HEARTBEAT PULSE -- */
@keyframes pulseGlow {
    0% { box-shadow: 0 0 5px rgba(255, 77, 129, 0.5); transform: scale(1); }
    50% { box-shadow: 0 0 25px rgba(255, 77, 129, 0.8); transform: scale(1.08); }
    100% { box-shadow: 0 0 5px rgba(255, 77, 129, 0.5); transform: scale(1); }
}

/* Apply this class to any button to make it breathe */
.pulse-button {
    animation: pulseGlow 2s infinite; 
}


/* -- THE SWIRLING FLOAT -- */
@keyframes floatMagic {
    0% {
        transform: translate(0, 0) scale(0.5) rotate(0deg);
        opacity: 0;
    }
    15% {
        opacity: 1;
    }
    50% {
        /* The var(--drift) is injected by JavaScript so each heart sways differently */
        transform: translate(calc(var(--drift) * 100px), -50vh) scale(1.2) rotate(180deg);
    }
    100% {
        transform: translate(calc(var(--drift) * 200px), -110vh) scale(1.5) rotate(360deg);
        opacity: 0;
    }
}

/* Apply this class to the spawned emojis */
.emoji-animated {
    position: absolute;
    bottom: -50px; /* Starts slightly below the screen */
    font-size: 2.5rem;
    animation: floatMagic 4s ease-in-out forwards;
}

```

### **2. The JavaScript (The Spawner)**

This script creates the HTML elements, gives them a random starting point, calculates their random wind "drift", and then cleans them up so the browser doesn't lag.

```javascript
// 1. Function to create a single floating emoji
function spawnSingleEmoji(char, container) {
    const el = document.createElement('div');
    el.classList.add('emoji-animated'); // Add the CSS class
    el.innerHTML = char;
    
    // Pick a random starting point horizontally across the screen
    el.style.left = Math.floor(Math.random() * window.innerWidth) + 'px';
    
    // Randomize how fast it flies up (between 3 to 5 seconds)
    el.style.animationDuration = (Math.random() * 2 + 3) + 's'; 
    
    // Create the random left/right drift variable used in the CSS @keyframes
    el.style.setProperty('--drift', Math.random() * 2 - 1); 
    
    container.appendChild(el);

    // Delete the element after 5 seconds to keep the website running fast
    setTimeout(() => {
        container.removeChild(el);
    }, 5000);
}

// 2. Function to trigger a massive burst of emojis
function triggerEmojiBurst(emojiArray, containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear any old animations
    
    // Spawn 50 emojis rapidly
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            // Pick a random emoji from the array provided
            let char = emojiArray[Math.floor(Math.random() * emojiArray.length)];
            spawnSingleEmoji(char, container);
        }, i * 80); // Wait 80 milliseconds between spawning each one
    }
}

/* HOW TO USE IT IN YOUR HTML:
  triggerEmojiBurst(['💖', '🌹', '✨'], 'myContainerId'); 
*/
```

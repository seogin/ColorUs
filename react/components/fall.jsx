{/** 
    Fall
    Color Characteristics: Warm, earthy, and rich. Autumn colors are deep and muted, reflecting the warmth and richness of the fall season with a golden undertone.
    Palette: Earthy tones and rich shades like rust, olive, burnt orange, and deep gold.
    Best Colors: Olive green (#808000), rust (#b7410e), burnt orange (#cc5500), and warm brown (#ae561c).
    */}

import React from "react";

const FallDetails = () => (
    <>
        <h2>Fall</h2>
        <p>
            Warm, earthy, and rich. Autumn colors are deep and muted, reflecting the warmth
            and richness of the fall season with a golden undertone.
        </p>
        <br />
        <p>
            Palette: Earthy tones and rich shades like rust, olive, burnt orange, and deep gold.
        </p>
        <br />
        <p>
            Best Colors:
            <ul>
                <li>Olive Green <span style={{ display: 'none' }}>(#808000)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#808000' }}></span></li>
                <li>Rust <span style={{ display: 'none' }}>(#b7410e)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#b7410e' }}></span></li>
                <li>Burnt Orange <span style={{ display: 'none' }}>(#cc5500)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#cc5500' }}></span></li>
                <li>Warm Brown <span style={{ display: 'none' }}>(#ae561c)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#ae561c' }}></span></li>
            </ul>
        </p>
    </>
);

export default FallDetails;

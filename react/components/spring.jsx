{/**
    Spring
    Color Characteristics: Warm, fresh, and lively. Spring colors are bright and clear, with a light, warm undertone that reflects the freshness of the season.
    Palette: Soft pastels and vibrant shades like peach, coral, warm yellow, and clear turquoise.
    Best Colors: Warm yellow (#fffba0), coral (#ff7f50), peach (#ffe5b4), mint green (#98ff98), and clear aqua (#c4e9e1).
    */}

import React from "react";

const SpringDetails = () => (
    <>
        <h2>Spring</h2>
        <p>
            Color Characteristics: Warm, fresh, and lively. Spring colors are
            bright and clear, with a light, warm undertone.
        </p>
        <br />
        <p>
            Palette: Soft pastels and vibrant shades like peach, coral, warm
            yellow, and clear turquoise.
        </p>
        <br />
        <p>
            Best Colors:
            <ul>
                <li>Warm Yellow (#ffb0a0) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#ffb0a0' }}></span></li>
                <li>Coral (#ff7750) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#ff7750' }}></span></li>
                <li>Peach (#ffe5b4) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#ffe5b4' }}></span></li>
                <li>Mint Green (#99ff98) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#99ff98' }}></span></li>
                <li>Clear Aqua (#c4e9e1) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#c4e9e1' }}></span></li>
            </ul>
        </p>
    </>
);

export default SpringDetails;

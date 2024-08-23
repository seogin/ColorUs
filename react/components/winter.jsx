{/**
    Winter
    Color Characteristics: Cool, deep, and bold. Winter colors are vivid and striking, with a cool, crisp quality that gives them intensity and drama.
    Palette: Intense, bold colors like black, true red, cobalt blue, and cool emerald.
    Best Colors: True red (#8f1d21), black (#000000), cobalt blue (#0047ab), and bright magenta (#ff08e8).
    */}

import React from "react";

const WinterDetails = () => (
    <>
        <h2>Winter</h2>
        <p>
            Cool, deep, and bold. Winter colors are vivid and striking, with a cool, crisp quality
            that gives them intensity and drama.
        </p>
        <br />
        <p>
            Palette: Intense, bold colors like black, true red, cobalt blue, and cool emerald.
        </p>
        <br />
        <p>
            Best Colors:
            <ul>
                <li>True Red <span style={{ display: 'none' }}>(#8f1d21)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#8f1d21' }}></span></li>
                <li>Black <span style={{ display: 'none' }}>(#000000)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#000000' }}></span></li>
                <li>Cobalt Blue <span style={{ display: 'none' }}>(#0047ab)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#0047ab' }}></span></li>
                <li>Bright Magenta <span style={{ display: 'none' }}>(#ff08e8)</span> <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#ff08e8' }}></span></li>
            </ul>
        </p>
    </>
);

export default WinterDetails;
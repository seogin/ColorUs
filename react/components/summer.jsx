{/** 
    Summer
    Color Characteristics: Cool, soft, and muted. Summer colors are gentle and soothing, with a cool undertone and a slightly faded, elegant quality.
    Palette: Delicate pastels and dusty shades like soft blue, lavender, rose, and dove gray.
    Best Colors: Powder blue (#b6d0e2), dusty rose (#dcae96), soft pink (#fdb0c0), and cool lavender (#e6e6fa).
    */}

import React from "react";

const SummerDetails = () => (
    <>
        <h2>Summer</h2>
        <p>
            Color Characteristics: Cool, soft, and muted.
            Summer colors are gentle and soothing, with a cool undertone and a slightly faded, elegant quality.
        </p>
        <br />
        <p>
            Palette: Delicate pastels and dusty shades like soft blue, lavender, rose, and dove gray.
        </p>
        <br />
        <p>
            Best Colors:
            <ul>
                <li>Powder Blue (#b6d0e2) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#b6d0e2' }}></span></li>
                <li>Dusty Rose (#dcae96) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#dcae96' }}></span></li>
                <li>Soft Pink (#fdb0c0) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#fdb0c0' }}></span></li>
                <li>Cool Lavender (#e6e6fa) <span style={{ display: 'inline-block', width: '16px', height: '16px', backgroundColor: '#e6e6fa' }}></span></li>
            </ul>
        </p>
    </>
);

export default SummerDetails;

:layout: landing

.. raw:: html

    <style>
        .full-width-banner {
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 4rem 0;
            background: linear-gradient(0deg,
                rgba(136, 180, 167, 0.5) 50%, 
                transparent 100%
            );
        }


        html {
            overflow-x: hidden;
            width: 100%;
        }

        .full-width-banner h1 {
            font-family: "Poppins", sans-serif;
            font-weight: 600;
            font-style: normal;
            color: #36454fff; /* default for light mode */
        }

        html.dark .full-width-banner h1 {
            color: #88b4a7ff; /* dark mode color */
        }

        .full-width-banner p {
            font-family: "Poppins", sans-serif;
            font-weight: 300;
            font-style: normal;
            color: #36454fff; /* default for light mode */
        }

        html.dark .full-width-banner p {
            color: #88b4a7ff; /* dark mode color */
        }

        .button {
            margin-left: 5px;
            margin-right: 5px; /* Adds 10px space to the right of the button */
        }

        a.button.reference.internal:hover {
            color: #88b4a7ff;   
        }

        a.button.reference.external {
            /* Additional external link styling */
            background-color: #36454fff;
            color: #ffffff;
            border: 2px solid #36454fff;
        }

        a.button.reference.external:hover {
            background-color: #ffffff;
            color: #36454fff;   
            border:2px solid #36454fff;
        }

        html.dark a.button.reference.external:hover {
            background-color: #000000;
        }

        .features {
            display: flex;
            justify-content: space-around;
            align-items: flex-start;
            gap: 2rem;
            margin: 2rem 0;
        }

        .features-section {
            text-align: center;
            margin: 4rem 0;
        }

        .features-section p {
            font-family: "Poppins", sans-serif;
            font-weight: 300;
            margin-top: 3rem;
        }

        .features-section h2 {
            font-family: "Poppins", sans-serif;
            font-weight: 600;
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
        }

        .feature {
            flex: 1;
            text-align: center;
            padding: 1rem;
        }

        @media (max-width: 768px) {
            .features {
                flex-direction: column;
                align-items: center; /* center content if desired */
            }
        }

        .feature h3 {
            font-family: "Poppins", sans-serif;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .feature p {
            font-family: "Poppins", sans-serif;
            font-weight: 300;
            margin-bottom: 0.5rem;
            font-size: 0.8rem;
        }

        html .light-img {
            display: block;
        }

        html .dark-img {
            display: none;
        }
        
        html.dark .dark-img {
            display: block;
        }
        
        html.dark .light-img {
            display: none;
        }
    </style>

    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    </head>

    <div class="full-width-banner" style="padding: 0; margin-bottom: 48px; height: calc(100vh - 56px - 48px); box-sizing: border-box;">
        <div class="hero-content" style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
            <img src="_static/logo.svg" alt="QuAIR Logo" style="transform: scale(0.3);">
            <h1 style="font-size: 7rem; margin-bottom: 0px">QuAIR-Platform</h1>
            <p style="font-size: 1.5rem;">Quantum AI Research Platforms</p>
            <div class="container buttons" style="margin-top: 64px">
                <a href="https://quair.group" class="button reference internal">Team</a>
                <a href="https://github.com/QuAIR" class="button reference external">GitHub</a>
            </div>
        </div>
    </div>

    <div class="features-section">
        <h2>Softwares</h2>
        <div class="features">
            <div class="feature">
               <h3>QuAIRKit</h3>
               <p>Python research framework for quantum computing, quantum information, and quantum machine learning algorithm development.</p>
            </div>
            <div class="feature">
               <h3>QRLab</h3>
               <p>MATLAB toolbox for exploring quantum information processing and quantum resource theory.</p>
            </div>
            <div class="feature">
               <h3>QuICK</h3>
               <p>Python QEC package (under construction) for code construction and decoding.</p>
            </div>
        </div>
    </div>
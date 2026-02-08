WCAG_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ==========================================================================
   Product-grade theme (ChatGPT-inspired, NOT a copy)
   Goals:
   - Consistent surface ladder
   - Deterministic colors (no "flip" after rerender)
   - WCAG 2.1 AAA for normal text where feasible (>= 7:1)
   - Strong focus visibility
   - Fix Gradio Chatbot wrappers (flex-wrap width/height 100% etc.)
   ========================================================================== */

:root{
  /* ---- Surfaces (light) ---- */
  --app-bg: #f7f7f8;          /* ChatGPT-like canvas */
  --panel-bg: #ffffff;        /* cards/panels */
  --panel-bg-2: #f1f5f9;      /* subtle elevated */
  --inset-bg: #eef2f7;        /* inset areas (chat canvas) */

  /* ---- Text (light) ---- */
  --text: #0f172a;            /* slate-900 */
  --text-muted: #334155;      /* slate-700 (AAA on white) */
  --text-subtle: #475569;

  /* ---- Borders / dividers ---- */
  --border: #cbd5e1;
  --border-strong: #94a3b8;

  /* ---- Accent (keep AAA with white text) ---- */
  --accent: #1e3a8a;          /* indigo-900-ish */
  --accent-hover: #1e40af;
  --accent-pressed: #172554;

  /* ---- Radii / shadows ---- */
  --r-xs: 10px;
  --r-sm: 12px;
  --r-md: 14px;
  --r-lg: 18px;

  --shadow-1: 0 1px 2px rgba(2,6,23,0.06);
  --shadow-2: 0 10px 26px rgba(2,6,23,0.10);
  --shadow-3: 0 16px 44px rgba(2,6,23,0.14);

  /* ---- Focus ring (AAA visible) ---- */
  --ring: #0f172a;

  /* ---- Spacing ---- */
  --s-1: 8px;
  --s-2: 12px;
  --s-3: 16px;
  --s-4: 20px;

  /* ---- Chat ---- */
  --chat-canvas: var(--inset-bg);
  --bubble-radius: 16px;
  --bubble-max: 92%;
  --bubble-max-px: 720px;

  --bubble-user-bg: var(--accent);
  --bubble-user-fg: #ffffff;

  --bubble-bot-bg: var(--panel-bg);
  --bubble-bot-fg: var(--text);
  --bubble-bot-border: rgba(15,23,42,0.12);

  --meta: var(--text-subtle);

  --action-bg: rgba(2,6,23,0.06);
  --action-border: rgba(15,23,42,0.18);
  --action-fg: var(--text);
}

@media (prefers-color-scheme: dark){
  :root{
    /* ---- Surfaces (dark) ---- */
    --app-bg: #0b0f19;        /* near-black */
    --panel-bg: #111827;      /* gray-900 */
    --panel-bg-2: #0f172a;    /* gray-950-ish */
    --inset-bg: #0b1220;      /* chat canvas */

    /* ---- Text (dark) ---- */
    --text: #f8fafc;
    --text-muted: #cbd5e1;
    --text-subtle: #cbd5e1;

    /* ---- Borders ---- */
    --border: #243044;
    --border-strong: #334155;

    /* ---- Accent (still AAA with white text) ---- */
    --accent: #1d4ed8;
    --accent-hover: #2563eb;
    --accent-pressed: #1e40af;

    /* ---- Shadows ---- */
    --shadow-1: 0 1px 2px rgba(0,0,0,0.28);
    --shadow-2: 0 16px 40px rgba(0,0,0,0.44);
    --shadow-3: 0 18px 56px rgba(0,0,0,0.55);

    /* ---- Focus ring ---- */
    --ring: #f8fafc;

    /* ---- Chat ---- */
    --bubble-bot-bg: #0f172a;       /* distinct from inset */
    --bubble-bot-fg: #f8fafc;
    --bubble-bot-border: #1f2a44;

    --action-bg: rgba(248,250,252,0.08);
    --action-border: #334155;
    --action-fg: #f8fafc;

    --meta: #cbd5e1;
  }
}

/* ==========================================================================
   Base
   ========================================================================== */
*{ font-family: 'Inter', sans-serif !important; }
.gradio-container{ max-width: 1200px !important; margin: 0 auto; }
body{
  background: var(--app-bg) !important;
  color: var(--text) !important;
}

/* ==========================================================================
   Header
   ========================================================================== */
.header-container{
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
  color: #ffffff;
  padding: 1.6rem 2rem;
  border-radius: var(--r-lg);
  margin-bottom: 1.5rem;
  border: 1px solid rgba(255,255,255,0.18);
  box-shadow: var(--shadow-3);
}
.header-container h1{
  margin: 0;
  color: #ffffff !important;
  font-weight: 800;
  letter-spacing: -0.02em;
}
.header-container p{
  margin-top: 6px;
  color: rgba(255,255,255,0.86) !important;
  font-weight: 600;
}

/* ==========================================================================
   Panels
   ========================================================================== */
.input-panel, .chat-panel{
  background: var(--panel-bg) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--r-lg) !important;
  padding: var(--s-4) !important;
  box-shadow: var(--shadow-2);
  color: var(--text) !important;
}

/* Left panel titles (use elem_id from app.py) */
#src_title, #src_title *{ color: var(--text) !important; }
#quick_guide, #quick_guide *{ color: var(--text-muted) !important; }


/* Links */
.input-panel a, .chat-panel a{
  color: var(--accent-hover) !important;
  text-decoration: underline !important;
  text-underline-offset: 3px;
}

/* ==========================================================================
   Inputs + Focus
   ========================================================================== */
textarea, input{
  background: var(--panel-bg) !important;
  color: var(--text) !important;
  border: 2px solid var(--border) !important;
  border-radius: var(--r-sm) !important;
  box-shadow: var(--shadow-1);
}
textarea::placeholder, input::placeholder{
  color: var(--text-subtle) !important;
  opacity: 0.9;
}
textarea:focus, input:focus{ border-color: var(--accent) !important; }

/* Visible focus (keyboard) */
button:focus-visible,
textarea:focus-visible,
input:focus-visible,
a:focus-visible{
  outline: 3px solid var(--ring) !important;
  outline-offset: 3px !important;
}

/* ==========================================================================
   Buttons (elem_id from app.py)
   ========================================================================== */
#btn-submit button{
  background: var(--accent) !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  border: 2px solid transparent !important;
  border-radius: var(--r-sm) !important;
  box-shadow: 0 14px 28px rgba(30,58,138,0.22);
  transition: transform 120ms ease, background 120ms ease;
}
#btn-submit button:hover{
  background: var(--accent-hover) !important;
  transform: translateY(-1px);
}
#btn-submit button:active{
  background: var(--accent-pressed) !important;
  transform: translateY(0px);
}

#btn-clear button{
  background: var(--panel-bg-2) !important;
  color: var(--text) !important;
  border: 2px solid var(--border) !important;
  font-weight: 800 !important;
  border-radius: var(--r-sm) !important;
  transition: transform 120ms ease, border-color 120ms ease;
}
#btn-clear button:hover{
  border-color: var(--border-strong) !important;
  transform: translateY(-1px);
}
#btn-clear button:active{ transform: translateY(0px); }

/* ==========================================================================
   File upload readability (left panel)
   ========================================================================== */
.input-panel [data-testid="block-label"],
.input-panel label,
.input-panel label *{
  color: var(--text) !important;
}

.input-panel .file-preview-holder td.filename,
.input-panel .file-preview-holder td.filename *{
  color: var(--text) !important;
  font-weight: 650 !important;
}
.input-panel .file-preview-holder td.download a,
.input-panel .file-preview-holder td.download a *{
  color: var(--text-muted) !important;
  text-decoration: underline !important;
  text-underline-offset: 3px !important;
}

@media (prefers-color-scheme: dark){
  /* Your requirement: white in dark mode */
  .input-panel [data-testid="block-label"],
  .input-panel label,
  .input-panel label *{
    color: #f8fafc !important;
    fill: #f8fafc !important;
    stroke: #f8fafc !important;
  }

  .input-panel .file-preview-holder td.filename,
  .input-panel .file-preview-holder td.filename *{
    color: #f8fafc !important;
  }
  .input-panel .file-preview-holder td.download a,
  .input-panel .file-preview-holder td.download a *{
    color: #e2e8f0 !important;
  }

  .input-panel button[aria-label="Clear"],
  .input-panel button[aria-label="Clear"] *{
    color: #f8fafc !important;
    stroke: #f8fafc !important;
  }

  .input-panel .file-preview-holder,
  .input-panel table,
  .input-panel tr,
  .input-panel td{
    background: transparent !important;
  }
}

/* ==========================================================================
   Chatbot (elem_id #chatbot) — fix Gradio wrappers + product bubbles
   ========================================================================== */

/* Chat canvas (scroll area). Gradio frequently uses .wrap.default.full */
#chatbot .wrap.default.full{
  background: var(--chat-canvas) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--r-lg) !important;
  padding: 16px !important;
}

/* IMPORTANT: Do NOT style each .message-wrap as a big card (causes giant blocks) */
#chatbot .message-wrap{
  background: transparent !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* Gradio applies "bubble" styles to the wrapper .flex-wrap.[user|bot]. Neutralize it. */
#chatbot .flex-wrap.user,
#chatbot .flex-wrap.bot{
  width: auto !important;
  height: auto !important;
  padding: 0 !important;
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  text-align: unset !important;
}

/* Row alignment */
#chatbot .message-row.user-row{
  display: flex !important;
  justify-content: flex-end !important;
}
#chatbot .message-row.bot-row{
  display: flex !important;
  justify-content: flex-start !important;
}

/* Bubble sizing */
#chatbot .message{
  width: auto !important;
  min-width: 280px !important;
  max-width: min(var(--bubble-max-px), var(--bubble-max)) !important;
  border-radius: var(--bubble-radius) !important;
  overflow: hidden !important;
  box-shadow: var(--shadow-2) !important;
}

/* panel-full-width must not force 100% */
#chatbot .message.panel-full-width{
  width: auto !important;
}

/* Deterministic content coloring (prevents “flip” on rerender) */
#chatbot .message button{
  background: transparent !important;
  border: 0 !important;
  width: 100% !important;
  color: inherit !important;
}
#chatbot .message .prose,
#chatbot .message .prose *{
  color: inherit !important;
}

/* Bubble colors */
#chatbot .message.user{
  background: var(--bubble-user-bg) !important;
  color: var(--bubble-user-fg) !important;
  border: 1px solid rgba(255,255,255,0.16) !important;
}
#chatbot .message.bot{
  background: var(--bubble-bot-bg) !important;
  color: var(--bubble-bot-fg) !important;
  border: 1px solid var(--bubble-bot-border) !important;
}

/* Typography (chat) */
#chatbot .message .prose{
  padding: 12px 14px !important;
  font-size: 0.98rem !important;
  line-height: 1.62 !important;
  white-space: normal !important;
  word-break: normal !important;
  overflow-wrap: break-word !important;
}
#chatbot .message .prose p{ margin: 0 !important; }

#chatbot .prose hr{
  border: 0;
  border-top: 1px solid rgba(148,163,184,0.45);
  margin: 10px 0;
}
#chatbot .prose em{
  color: var(--meta) !important;
  font-style: normal !important;
  font-weight: 700 !important;
}

/* Links inside bubbles */
#chatbot .message.user .prose a{ color: #ffffff !important; }
#chatbot .message.bot  .prose a{ color: var(--accent-hover) !important; }

/* Code styling */
#chatbot .prose code{
  padding: 0.12rem 0.38rem !important;
  border-radius: 9px !important;
  border: 1px solid rgba(148,163,184,0.28) !important;
  background: rgba(148,163,184,0.16) !important;
}
#chatbot .message.user .prose code{
  background: rgba(255,255,255,0.16) !important;
  border-color: rgba(255,255,255,0.22) !important;
}

/* Copy buttons */
#chatbot .message-buttons button.action{
  border-radius: 10px !important;
  border: 1px solid var(--action-border) !important;
  background: var(--action-bg) !important;
  color: var(--action-fg) !important;
}
#chatbot .message-buttons button.action:focus-visible{
  outline: 3px solid var(--ring) !important;
  outline-offset: 3px !important;
}
/* =========================================================
   LEFT PANEL — testo sempre nero (pannello bianco)
   ========================================================= */

/* Documento Sorgente */
.input-panel #src_title,
.input-panel #src_title *{
  color: #0f172a !important; /* nero leggibile, AAA su bianco */
}

/* Guida Rapida */
.input-panel #quick_guide,
.input-panel #quick_guide *{
  color: #0f172a !important;
}

/* Titolo "Guida Rapida:" leggermente più forte */
.input-panel #quick_guide strong{
  color: #020617 !important;
  font-weight: 700 !important;
}

"""

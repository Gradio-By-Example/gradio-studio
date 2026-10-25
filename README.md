# Gradio Sketch

Visual Gradio app builder that shipped with Gradio 5.x as `gradio sketch`.

Gradio 6 removed that command. This package archives the sketch-only code from **Gradio 5.49.1** (the last tagged 5.x release in this repository that still included it) and runs it against current Gradio 6 components instead of vendoring Gradio itself.

Vibe Editor is separate: Gradio 6 still provides it as `gradio --vibe`. This archive restores the layout/event sketch UI, not the vibe editor.

## Install

From the Gradio repository root, with Gradio already installed in development mode:

```bash
pip install -e ./gradio_sketch --no-deps
gradio cc build ./gradio_sketch --no-generate-docs
```

`--no-deps` keeps your local Gradio checkout instead of installing Gradio from PyPI. If you use a released Gradio 6 wheel, a normal `pip install -e ./gradio_sketch` is fine.

`gradio cc build` compiles the `SketchBox` overlay (the only frontend that belongs to sketch) into this package. Gradio components such as `Textbox`, `Row`, and `Sidebar` are imported from the installed `gradio` package.

## Run

```bash
gradio sketch
# or
gradio-sketch
# or
python -m gradio_sketch
```

Optional argument: the Python file to generate (default `app.py`).

## Layout

- `backend/gradio_sketch/run.py` — sketch app, using `import gradio as gr`
- `backend/gradio_sketch/sketchbox.py` — overlay layout component
- `backend/gradio_sketch/utils.py` — code-generation helpers
- `frontend/` — `SketchBox` Svelte UI only

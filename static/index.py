import js

canvas = js.document.getElementById("can")
gl = canvas.getContext("webgl")

if not gl:
    print("Unable to use webgl :c")
else:
    gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight)
    gl.clearColor(0.0, 0.5, 0.0, 1.0)
    gl.clear(gl.COLOR_BUFFER_BIT)



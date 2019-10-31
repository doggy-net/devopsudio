function drawRoundedRect(ctx, x, y, width, height, radius) {
  const path = new Path2D();

  path.moveTo(x + radius, y);
  path.lineTo(x + width - radius, y);
  path.arc(x + width - radius, y + radius, radius, Math.PI / 180 * 270, 0, false);
  path.lineTo(x + width, y + height - radius);
  path.arc(x + width - radius, y + height - radius, radius, 0, Math.PI / 180 * 90, 0, false);
  path.lineTo(x + radius, y + height);
  path.arc(x + radius, y + height - radius, radius, Math.PI / 180 * 90, Math.PI / 180 * 180, false);
  path.lineTo(x, y + radius);
  path.arc(x + radius, y + radius, radius, Math.PI / 180 * 180, Math.PI / 180 * 270, false);
  ctx.stroke(path);
}

function drawBorderedText(ctx, text, x, y) {
  const textBaseline = ctx.textBaseline;
  ctx.textBaseline = 'hanging';
  const devicePixelRatio = window.devicePixelRatio || 1;
  const textWidth = ctx.measureText(text).width * devicePixelRatio;
  const textHeight = parseInt(ctx.font.match(/\d+/), 10) * devicePixelRatio;
  const radius = 16 * devicePixelRatio;
  ctx.fillText(text, x + radius, y);
  drawRoundedRect(ctx, x, y, textWidth + radius * 2, textHeight, radius);
  ctx.textBaseline = textBaseline;
}

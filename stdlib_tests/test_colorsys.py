import colorsys


print(colorsys.rgb_to_hls(256, 0, 0))
print(colorsys.hls_to_rgb(*colorsys.rgb_to_hls(256, 0, 0)))

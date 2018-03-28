import mapnik
m = mapnik.Map(1200,700)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ED5503')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 30.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:/New folder/New folder/IND_KOT_text.shp")
layer = mapnik.Layer('world')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'indokotatext.jpeg', 'jpeg')
print "rendered image to 'indokotatext.jpeg'"
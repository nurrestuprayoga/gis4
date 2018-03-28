import mapnik
m = mapnik.Map(1080,720)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 20.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:/New folder/New folder/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'provinsi.png', 'png')
print "rendered image to 'provinsi.png'"

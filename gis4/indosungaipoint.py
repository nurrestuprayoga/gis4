import mapnik
m = mapnik.Map(3200,1200)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FC29A0')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 2)
line_symbolizer.stroke_width = 50.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:/New folder/New folder/IND_SNG_point.shp")
layer = mapnik.Layer('world')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'indosungaipoint.png', 'png')
print "rendered image to 'indosungaipoint.jpg'"
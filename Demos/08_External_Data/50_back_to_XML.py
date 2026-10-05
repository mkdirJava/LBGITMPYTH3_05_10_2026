import xml.dom.minidom
doc = xml.dom.minidom.parse('accounts4.xml')

out = open('new.xml', 'w')
doc.writexml(out)	       	# Save it
out.close()

print(doc.toxml())		# Display it on stdout

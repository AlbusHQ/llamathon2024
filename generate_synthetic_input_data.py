import xml.etree.ElementTree as ET

### this is the XML for House
xml_data = '''<?xml version="1.0" encoding="UTF-8"?> 
<java version="1.5.0_02" class="java.beans.XMLDecoder"> 
 <object class="oripa.DataSet"> 
  <void property="lines"> 
   <array class="oripa.OriLineProxy" length="22"> 
    <void index="0"> 
     <object class="oripa.OriLineProxy"> 
      <void property="type"> 
       <int>1</int> 
      </void> 
      <void property="x0"> 
       <double>200.0</double> 
      </void> 
      <void property="x1"> 
       <double>200.0</double> 
      </void> 
      <void property="y0"> 
       <double>200.0</double> 
      </void> 
      <void property="y1"> 
       <double>100.0</double> 
      </void> 
     </object> 
    </void> 
    <void index="1"> 
     <object class="oripa.OriLineProxy"> 
      <void property="type"> 
       <int>1</int> 
      </void> 
      <void property="x0"> 
       <double>-200.0</double> 
      </void> 
      <void property="x1"> 
       <double>-200.0</double> 
      </void> 
      <void property="y0"> 
       <double>200.0</double> 
      </void> 
      <void property="y1"> 
       <double>100.0</double> 
      </void> 
     </object> 
    </void> 
    <void index="2"> 
     <object class="oripa.OriLineProxy"> 
      <void property="type"> 
       <int>1</int> 
      </void> 
      <void property="x0"> 
       <double>-200.0</double> 
      </void> 
      <void property="x1"> 
       <double>-100.0</double> 
      </void> 
      <void property="y0"> 
       <double>200.0</double> 
      </void> 
      <void property="y1"> 
       <double>200.0</double> 
      </void> 
     </object> 
    </void> 
    <void index="3"> 
     <object class="oripa.OriLineProxy"> 
      <void property="type"> 
       <int>3</int> 
      </void> 
      <void property="x0"> 
       <double>-200.0</double> 
      </void> 
      <void property="x1"> 
       <double>-100.0</double> 
      </void> 
      <void property="y0"> 
       <double>100.0</double> 
      </void> 
      <void property="y1"> 
       <double>100.0</double> 
      </void> 
     </object> 
    </void> 
    <void index="4"> 
     <object class="oripa.OriLineProxy"> 
      <void property="type"> 
       <int>2</int> 
      </void> 
      <void property="x0"> 
       <double>-100.0</double> 
      </void> 
      <void property="x1"> 
       <double>-100.0</double> 
      </void> 
      <void property="y0"> 
       <double>100.0</double> 
      </void> 
      <void property="y1"> 
       <double>200.0</double> 
      </void> 
     </object> 
    </void> 
    <!-- More XML lines here --> 
   </array> 
  </void> 
  <void property="mainVersion"> 
   <int>1</int> 
  </void> 
  <void property="paperSize"> 
   <double>400.0</double> 
  </void> 
 </object> 
</java>'''

# Parse the XML data
root = ET.fromstring(xml_data)

# Find all lines
lines = root.findall(".//void[@property='lines']//object")

# Define a dictionary to map int values to strings
line_types = {
    1: "auxiliary line",
    2: "mountain fold",
    3: "valley fold"
}

# Function to generate labels A, B, ..., Z, AA, AB, ..., ZZ, etc.
def generate_labels(n):
    labels = []
    while n >= 0:
        label = ""
        while True:
            n, r = divmod(n, 26)
            label = chr(65 + r) + label
            if n == 0:
                break
            n -= 1
        labels.append(label)
        n -= 1
    return labels[::-1]

# Generate labels for the points
num_lines = len(lines)
labels = generate_labels(num_lines * 2 - 1)

# Print the lines with labels and types
for i, line in enumerate(lines):
    line_type = int(line.find(".//void[@property='type']/int").text)
    x0 = line.find(".//void[@property='x0']/double").text
    y0 = line.find(".//void[@property='y0']/double").text
    x1 = line.find(".//void[@property='x1']/double").text
    y1 = line.find(".//void[@property='y1']/double").text
    start_label = labels[i * 2]
    end_label = labels[i * 2 + 1]
    print(f"{start_label} ({x0}, {y0}) to {end_label} ({x1}, {y1}): {line_types.get(line_type, 'Unknown type')}")


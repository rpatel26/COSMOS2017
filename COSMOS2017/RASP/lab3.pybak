file = pickAFile()
pic = makePicture( file )

def whileGray( picture ):
  pix = getPixels( picture )
  pixLen = len( pix )
  i = 0
  while i < pixLen:
    r = getRed( pix[i] )
    g = getGreen( pix[i] )
    b = getBlue( pix[i] )
    luminance = ( r + g + b ) / 3
    luminance = makeColor( luminance, luminance, luminance )
    setColor( pix[i], luminance )
    i = i + 1
    
  show( picture )
  
def nestedGray( picture ):
  width = getWidth( picture )
  height = getHeight( picture )
  
  for col in range( height ):
    for row in range( width ):
      pix = getPixel( picture, row, col )
      r = getRed( pix )
      g = getGreen( pix )
      b = getBlue( pix )
      luminance = ( r + g + b ) / 3
      grayColor = makeColor( luminance, luminance, luminance )
      setColor( pix, grayColor )
  
  show( picture )


nestedGray( pic )
file = pickAFile()
pic = makePicture( file )
copy = duplicatePicture( pic )

show( pic )

def makeAverageColor( picture ):
  pix = getPixels( picture )
  redSum = 0
  blueSum = 0
  greenSum = 0
  pixLen = len( pix )
  
  for i in range( pixLen ):
    redSum = getRed( pix[i] )
    greenSum = getGreen( pix[i] )
    blueSum = getBlue( pix[i] )
    # NOTE: the above code contains error, fix is 
    #  illustrated below
    # redSum = redSum + getRed( pix[i] )
    # greenSum = greenSum + getGreen( pix[i] )
    # blueSum = blueSum = getBlue( pix[i] )
    
  averageRed = redSum / pixLen
  averageGreen = greenSum / pixLen
  averageBlue = blueSum / pixLen
  
  for i in range( pixLen ):
    newColor = makeColor( averageRed, averageGreen, averageBlue )
    setColor( pix[i], newColor )
  
  show( picture )
  
## Second half of lab starts here


LIGHT_GREY = (220,220,220)
ORANGE = (255,128,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
LIGHT_BLUE = (0,255,255)

class Planet:    
    def __init__(self, name, mass, diameter, density, gravity, escVelocity, rotationPeriod, dayLength, fromSun, perihelion, apheleon, orbitPeriod, orbitVelocity, orbitInclination, orbitEccentricity, obliquityToOrbit, temp, surfacePressure, moons, ringsys, gmf, img, colour, atmosphereComp):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.escVelocity = escVelocity
        self.rotationPeriod = rotationPeriod
        self.dayLength = dayLength
        self.fromSun = fromSun
        self.perihelion = perihelion
        self.apheleon = apheleon 
        self.orbitPeriod = orbitPeriod
        self.orbitVelocity = orbitVelocity
        self.orbitInclination = orbitInclination
        self.orbitEccentricity	= orbitEccentricity
        self.obliquityToOrbit = obliquityToOrbit
        self.temp = temp
        self.surfacePressure = surfacePressure
        self.moons = moons	
        self.ringsys = ringsys
        self.gmf = gmf
        self.img = img
        self.colour = colour
        self.atmosphereComp = atmosphereComp

mercury = Planet("Mercury",0.33*10**24,4879,5429,3.7,4.3,1407.6,4222.6,57.9*10**6,46*10**6,69.8*10**6,88,47.4,7,0.206,0.034,167,0,0,False,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/mercury.gif",LIGHT_GREY,{"Oxygen":0.42,"Sodium":0.22,"Hydrogen":0.22,"Helium":0.06,"Other":0.08 })
venus = Planet("Venus",4.87*10**24,12104,5243,8.9,10.4,-5832.5,2802,108.2*10**6,107.5*10**6,108.9*10**6,224.7,35,3.4,0.007,177.4,464,92,0,False,False,"https://nssdc.gsfc.nasa.gov/planetary/image/venus.jpg",ORANGE,{"Carbon Dioxide":0.965,"Nitrogen":0.035})
earth = Planet("Earth",5.97*10**24,12756,5514,9.8,11.2,23.9,24,149.6*10**6,147.1*10**6,152.1*10**6,365.2,29.8,0,0.017,23.4,15,1,1,False,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/earth.gif",BLUE,{"Nitrogen":0.7808,"Oxygen":0.2095,"Other":0.0097})
moon = Planet("Moon",0.073*10**24,3475,3340,1.6,2.4,655.7,708.7,0.384*10**6,0.363*10**6,0.406*10**6,27.3,1,5.1,0.055,6.7,-20,0,0,False,False,"https://nssdc.gsfc.nasa.gov/planetary/banner/moon.gif",LIGHT_GREY,{"Argon":0.7,"Helium":0.29,"Sodium":0.01})
mars = Planet("Mars",0.642*10**24,6792,3934,3.7,5,24.6,24.7,228*10**6,206.7*10**6,249.3*10**6,687,24.1,1.8,0.094,25.2,-65,0.01,2,False,False,"https://nssdc.gsfc.nasa.gov/planetary/banner/mars.gif",RED,{"Carbon Dioxide":0.951,"Nitrogen":0.0259,"Argon":0.0194,"Oxygen":0.0016,"Carbon Monoxide":0.0006,"Other":0.0015})
jupiter = Planet("Jupiter",1898*10**24,142984,1326,23.1,59.5,9.9,9.9,778.5*10**6,740.6*10**6,816.4*10**6,4331,13.1,1.3,0.049,3.1,-110,None,79,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/jupiter.gif",ORANGE,{"Molecular Hydrogen":0.898,"Helium":0.102})
saturn = Planet("Saturn",568*10**24,120536,687,9,35.5,10.7,10.7,1432*10**6,1357.6*10**6,1506.5*10**6,10747,9.7,2.5,0.052,26.7,-140,None,82,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/saturn.gif",YELLOW,{"Molecular Hydrogen":0.963,"Helium":0.0325,"Other":0.0045})
uranus = Planet("Uranus",86.8*10**24,51118,1270,8.7,21.3,-17.2,17.2,2867*10**6,2732.7*10**6,3001.4*10**6,30589,6.8,0.8,0.047,97.8,-195,None,27,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/uranus.gif",BLUE,{"Molecular Hydrogen":0.825,"Helium":0.152,"Other":0.023})
neptune = Planet("Neptune",102*10**24,49528,1638,11,23.5,16.1,16.1,4515*10**6,4471.1*10**6,4558.9*10**6,59800,5.4,1.8,0.01,28.3,-200,None,14,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/neptune.gif",BLUE,{"Molecular Hydrogen":0.8,"Helium":0.19,"Methane":0.01})
pluto = Planet("Pluto",0.013*10**24,2376,1850,0.7,1.3,-153.3,153.3,5906.4*10**6,4436.8*10**6,7375.9*10**6,90560,4.7,17.2,0.244,122.5,-225,0.00001,5,False,None,"https://nssdc.gsfc.nasa.gov/planetary/banner/plutofact.gif",LIGHT_BLUE,{"Nitrogen":0.99,"Methane":0.005,"Carbon Monoxide":0.0005,"Other":0.0045})

planets=[mercury,venus,earth,moon,mars,jupiter,saturn,uranus,neptune,pluto]
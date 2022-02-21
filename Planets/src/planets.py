# Mass (kg), Diameter (km), Density (kg/m3), Gravity (m/s2), Escape Velocity (km/s), Rotation Period (hours),
# Length of Day (hours), Distance from Sun (106 km), Perihelion (106 km), Aphelion (106 km), Orbital Period (days),
# Orbital Velocity (km/s), Orbital Inclination (degrees), Orbital Eccentricity, Obliquity to Orbit (degrees),Mean Temperature (C),
# Surface Pressure (bars),Number of Moons,Ring System, Global Magnetic Field

class Planet:
    def __init__(self, mass, diameter, density, gravity, escVelocity, rotationPeriod, dayLength, fromSun, perihelion, apheleon, orbitPeriod, orbitVelocity, orbitInclination, orbitEccentricity, obliquityToOrbit, temp, surfacePressure, moons, ringsys, gmf, img):
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

mercury = Planet(0.33*10**24,4879,5429,3.7,4.3,1407.6,4222.6,57.9*10**6,46*10**6,69.8*10**6,88,47.4,7,0.206,0.034,167,0,0,False,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/mercury.gif")
venus = Planet(4.87*10**24,12104,5243,8.9,10.4,-5832.5,2802,108.2*10**6,107.5*10**6,108.9*10**6,224.7,35,3.4,0.007,177.4,464,92,0,False,False,"https://nssdc.gsfc.nasa.gov/planetary/image/venus.jpg")
earth = Planet(5.97*10**24,12756,5514,9.8,11.2,23.9,24,149.6*10**6,147.1*10**6,152.1*10**6,365.2,29.8,0,0.017,23.4,15,1,1,False,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/earth.gif")
moon = Planet(0.073*10**24,3475,3340,1.6,2.4,655.7,708.7,0.384*10**6,0.363*10**6,0.406*10**6,27.3,1,5.1,0.055,6.7,-20,0,0,False,False,"https://nssdc.gsfc.nasa.gov/planetary/banner/moon.gif")
mars = Planet(0.642*10**24,6792,3934,3.7,5,24.6,24.7,228*10**6,206.7*10**6,249.3*10**6,687,24.1,1.8,0.094,25.2,-65,0.01,2,False,False,"https://nssdc.gsfc.nasa.gov/planetary/banner/mars.gif")
jupiter = Planet(1898*10**24,142984,1326,23.1,59.5,9.9,9.9,778.5*10**6,740.6*10**6,816.4*10**6,4331,13.1,1.3,0.049,3.1,-110,None,79,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/jupiter.gif")
saturn = Planet(568*10**24,120536,687,9,35.5,10.7,10.7,1432*10**6,1357.6*10**6,1506.5*10**6,10747,9.7,2.5,0.052,26.7,-140,None,82,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/saturn.gif")
uranus = Planet(86.8*10**24,51118,1270,8.7,21.3,-17.2,17.2,2867*10**6,2732.7*10**6,3001.4*10**6,30589,6.8,0.8,0.047,97.8,-195,None,27,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/uranus.gif")
neptune = Planet(102*10**24,49528,1638,11,23.5,16.1,16.1,4515*10**6,4471.1*10**6,4558.9*10**6,59800,5.4,1.8,0.01,28.3,-200,None,14,True,True,"https://nssdc.gsfc.nasa.gov/planetary/banner/neptune.gif")
pluto = Planet(0.013*10**24,2376,1850,0.7,1.3,-153.3,153.3,5906.4*10**6,4436.8*10**6,7375.9*10**6,90560,4.7,17.2,0.244,122.5,-225,0.00001,5,False,None,"https://nssdc.gsfc.nasa.gov/planetary/banner/plutofact.gif")
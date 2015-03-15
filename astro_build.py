import math, itertools, sys, datetime


## values and abbrevations taken from http://www.stjarnhimlen.se/comp/ppcomp.html

def calculate_day(year, month, day, hour):
    return 367*year - 7 * ( year + (month+9)/12 ) / 4 + 275*month/9 + day - 730530 + float(hour)/float(24)

def get_planet(name, d):

    if name == "Sun":
      return { 
         'N': math.radians(0.0),
         'i' : math.radians(0.0),
         'w' : math.radians(282.9404 + 4.70935E-5 * d),
         'a' : 1.000000,
         'e' : 0.016709 - 1.151E-9 * d,
         'M' : math.radians(356.0470 + 0.9856002585 * d)
        }
    elif name == 'Mercury':
        return { 
         'N': math.radians(48.3313 + 3.24587E-5 * d),
         'i' :  math.radians(7.0047 + 5.00E-8 * d),
         'w' : math.radians(29.1241 + 1.01444E-5 * d),
         'a' : 0.387098,
         'e' : 0.205635 + 5.59E-10 * d,
         'M' : math.radians(168.6562 + 4.0923344368 * d)
        }
    elif name == 'Venus':
        return { 
         'N' : math.radians(76.6799 + 2.46590E-5 * d),
         'i' : math.radians(3.3946 + 2.75E-8 * d),
         'w' : math.radians(54.8910 + 1.38374E-5 * d),
         'a' : 0.723330,
         'e' : 0.006773 - 1.302E-9 * d,
         'M' : math.radians(48.0052 + 1.6021302244 * d)
        }
    elif name == 'Mars':
       return {
         'N': math.radians(49.5574 + 2.11081E-5 * d),
         'i' : math.radians(1.8497 - 1.78E-8 * d),
         'w' : math.radians(286.5016 + 2.92961E-5 * d),
         'a' : 1.523688,
         'e' : 0.093405 + 2.516E-9 * d,
         'M' : math.radians(18.6021 + 0.5240207766 * d)
        }
    elif name == 'Jupiter':
        return { 
         'N': math.radians(100.4542 + 2.76854E-5 * d),
         'i' : math.radians(1.3030 - 1.557E-7 * d),
         'w' : math.radians(273.8777 + 1.64505E-5 * d),
         'a' : 5.20256,
         'e' : 0.048498 + 4.469E-9 * d,
         'M' : math.radians(19.8950 + 0.0830853001 * d)
        }
    elif name == 'Saturn':
        return { 
         'N': math.radians(113.6634 + 2.38980E-5 * d),
         'i' : math.radians(2.4886 - 1.081E-7 * d),
         'w' : math.radians(339.3939 + 2.97661E-5 * d),
         'a' : 9.55475,
         'e' : 0.055546 - 9.499E-9 * d,
         'M' : math.radians(316.9670 + 0.0334442282 * d)
        }               
    elif name == 'Uranus':
      return { 
         'N': math.radians(74.0005 + 1.3978E-5 * d),
         'i' : math.radians( 0.7733 + 1.9E-8 * d),
         'w' : math.radians(96.6612 + 3.0565E-5 * d),
         'a' : 19.18171 - 1.55E-8 * d,
         'e' : 0.047318 + 7.45E-9 * d,
         'M' : math.radians(142.5905 + 0.011725806 * d) 
        }       
    elif name == 'Neptune':
      return { 
         'N': math.radians(131.7806 + 3.0173E-5 * d),
         'i' : math.radians(1.7700 - 2.55E-7 * d),
         'w' : math.radians(272.8461 - 6.027E-6 * d),
         'a' : 30.05826 + 3.313E-8 * d,
         'e' : 0.008606 + 2.15E-9 * d,
         'M' : math.radians(260.2471 + 0.005995147 * d)
        }


def calc_orbital_elements(planet_name, d):

    planet = get_planet(planet_name, d)

    N = planet.get('N')
    i = planet.get('i')
    w = planet.get('w')
    a = planet.get('a')
    e = planet.get('e')
    M = planet.get('M')

    E = M + e* math.sin(M) * ( 1.0 + e * math.cos(M) )

    xv =  a * ( math.cos(E) - e )
    yv =  a * ( math.sqrt(1.0 - e*e) * math.sin(E) )

    v = math.atan2( yv, xv )
    r = math.sqrt( xv*xv + yv*yv )

    xh = r * ( math.cos(N) * math.cos(v+w) - math.sin(N) * math.sin(v+w) * math.cos(i) )
    yh = r * ( math.sin(N) * math.cos(v+w) + math.cos(N) * math.sin(v+w) * math.cos(i) )
    zh = r * ( math.sin(v+w) * math.sin(i) )

    lonecl = math.atan2( yh, xh )
    latecl = math.atan2( zh, math.sqrt(xh*xh+yh*yh) )

    return {
        'r' : r,
        'v' : v,
        'xh' : xh,
        'yh' : yh,
        'w'  :w,
        'lonecl' : lonecl,
        'latecl ': latecl

    }


def calc_geocentric_alignments(planet_name, d):

    sun = calc_orbital_elements('Sun', d)
    planet = calc_orbital_elements(planet_name, d)

    lonsun = sun.get('v') + sun.get('w')

    xs = sun.get('r') * math.cos(lonsun)
    ys = sun.get('r') * math.sin(lonsun)

    xh = planet.get('xh')
    yh = planet.get('yh')

    xg = xh + xs
    yg = yh + ys

    helio_degree = math.degrees(math.atan2( xh, yh ))
    geo_degree = math.degrees(math.atan2( xg, yg ))


    helio_degree =  90 - helio_degree
    geo_degree = 90 - geo_degree

    if helio_degree < 0:
        helio_degree = helio_degree + 360
    if geo_degree < 0:
        geo_degree = geo_degree + 360

    return geo_degree


def check_alignments(alignments):

    for degree, grouped in itertools.groupby(alignments,  lambda x: x[1]):
        planets = map(lambda x: x[0], grouped)
        if len(planets) > 1:
            sys.stderr.write("BUILD FAILED" + '\n')
            sys.stderr.write("PLANETS ALIGNED: " + str(planets)+'\n')
            sys.stderr.write("ALIGNMENT: " + str(int(degree)) +' degrees\n') 
            sys.exit(1)
            
    sys.stdout.write('NO PLANETS ALIGNED\n')


def main():

    now = datetime.datetime.utcnow()
    d = calculate_day(now.year, now.month, now.day, now.hour)

    planet_names = ['Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    alignments = map(lambda x: [x, round(calc_geocentric_alignments(x, d))], planet_names)
    alignments.sort(key= lambda x: x[1])

    check_alignments(alignments)


main()

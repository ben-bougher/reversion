import webapp2
from os.path import join, dirname
from jinja2 import Environment, FileSystemLoader

import os
import csv

env = Environment(loader=FileSystemLoader(join(dirname(__file__),
                                               'templates')))
image_dir  = "static/images"

def filename(w,n,n_tot):

    return os.path.join(image_dir, "Bond.png")



            
class MainHandler(webapp2.RequestHandler):

    def get(self):
        
        # Slider limits
        wmin = 1
        wmax = 30
        wstep = 1
        
        imax = 10
        imin = 1
        istep = 1

        misfit = []
        with open('misfit.txt', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                misfit.append(float(row[0]))
                
        
        template = env.get_template("xplore.html")
        html = template.render(wmin=wmin, wmax=wmax, wstep=wstep,
                               imin=imin, imax=imax, istep=istep,
                               misfit=misfit)


        
        self.response.write(html)





app  = webapp2.WSGIApplication([
    ('/', MainHandler),],
    debug=True)



def main():
    from paste import httpserver
    httpserver.serve(app,host='127.0.0.1', port='8080')

    
if __name__ == '__main__':
    main()    

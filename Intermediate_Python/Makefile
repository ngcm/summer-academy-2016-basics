# Simple Makefile for building teaching material as a static html slideshow

FLAGS=--ExecutePreprocessor.enabled=True --ExecutePreprocessor.allow_errors=True\
		--ExecutePreprocessor.timeout=300

NOTEBOOKS=exercises/01-dtypes.html exercises/02-Classes_basics.html \
		  exercises/03-Classes_pt2.html exercises/04-Predator_prey.html \
		  soln/01-dtypes.html soln/02-Classes_basics.html \
		  soln/03-Classes_pt2.html soln/04-Predator_prey.html \

slides:
	jupyter nbconvert --to slides $(FLAGS) index

serve:
	jupyter nbconvert --to slides $(FLAGS) index --post serve

html: $(NOTEBOOKS)
	jupyter nbconvert --to html $(FLAGS) index

%.html: %.ipynb
	jupyter nbconvert --to html $(FLAGS) $< --output $@

clean:
	rm index.slides.html
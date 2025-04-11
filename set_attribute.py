#!/usr/bin/env python3
# coding=utf-8

import inkex

class SetAttributeExtension(inkex.EffectExtension):

    def add_arguments(self, pars):
        pars.add_argument(
            "--attribute_name",
            default="class",
            help="the attribute name",
        )
        pars.add_argument(
            "--attribute_value",
            default="",
            help="the attribute value",
        )


    def effect(self):

        # Check for a single object selection
        if len(self.svg.selected) != 1:
            inkex.errormsg("Please select exactly one object.")
            return

        # Retrieve the selected element
        element = list(self.svg.selected.values())[0]
        current_class = element.get(self.options.attribute_name, "")

        # Set the (new) class attribute on the selected element
        element.set(self.options.attribute_name, self.options.attribute_value )
        #element.set("class", "yeah")
        

if __name__ == '__main__':
    SetAttributeExtension().run()

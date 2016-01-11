'''
Created on

@author: raniba
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Run picard tool AddOrReplaceReadGroup, load dependencies and requirements
    '''
    def __init__(self, component_name='reheader', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        generate the AddOrReplaceReadGroup command
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        rehead_jar = self.requirements['picard']
        rehead_infile = self.args.infile
        rehead_outfile = self.args.outfile

        basename = os.path.basename(rehead_infile)
        bam_id = basename.split(".bam")[0]

        cmd = self.requirements['java']
        cmd_args = [
            java_mem,
            java_jar_option,
            rehead_jar,
            "INPUT=" + rehead_infile,
            "OUTPUT=" + rehead_outfile,
            "SORT_ORDER=coordinate",
            "RGLB=8",
            "RGPL=Illumina",
            "RGPU=1",
            "RGSM=" + bam_id,
            "VALIDATION_STRINGENCY=LENIENT"
        ]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    rehead = Component()
    rehead.args = component_ui.args
    rehead.run()

if __name__ == '__main__':

    import component_ui

    _main()

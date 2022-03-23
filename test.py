from mantid.simpleapi import DeleteWorkspace, LoadDiffCal
from mantid.api import AnalysisDataService
import pooch


def get_file():
    return pooch.create(
        path=pooch.os_cache('test-loaddiffcal'),
        base_url='https://public.esss.dk/groups/scipp/ess/powgen/1/',
        registry={
            'PG3_FERNS_d4832_2011_08_24.cal': 'md5:c181221ebef9fcf30114954268c7a6b6'
        }).fetch('PG3_FERNS_d4832_2011_08_24.cal')


def main():
    ws = LoadDiffCal(Filename=str(get_file()),
                     InstrumentFilename='POWGEN_Definition_2011-02-25.xml',
                     WorkspaceName='ws',
                     MakeGroupingWorkspace=False)
    print('loaded')
    for name in AnalysisDataService.Instance().getObjectNames():
        if name.startswith('ws'):
            DeleteWorkspace(name)
    print('deleted')


if __name__ == '__main__':
  main()

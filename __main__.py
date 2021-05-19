import sys
from argparse import ArgumentParser
from .core import parser_loader, ForecastType, Unit


def validate_forecast_args(args):
    if args.forecast_option is None:
        err = ('At least one argument must be included: '
               '-td/--today, -5d/--weekdays, -10d/--tendays, -w/--weekend')
        print(f'{argparser.prog}: error: {err}', file=sys.stderr)
        sys.exit()

parsers = parser_loader.load('./parsers')

argparser = ArgumentParser(prog='flask-weather-app',
                           description='Weather info via APIs right on your terminal')

required = argparser.add_argument_group('required arguments')
required.add_argument('-p', '--parser', choices=parsers.keys(), required=True,
                      dest='parser', help=('Specify which parser to use for scraping.'))

# grab all enums
unit_values = [name.title() for name, value in
               Unit.__members__.items()]

argparser.add_argument('-u', '--unit', choices=unit_values, required=False,
                       dest='unit', help=('Specify unit of measurement for temperature.'))

required.add_argument('-a', '--areacode', required=True, dest='area_code',
                      help=('The code for the region to get the weather for.'))

argparser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

argparser.add_argument('-td', '--today', dest='forecast_option', action='store_const',
                       const=ForecastType.TODAY, help='Get forecast for today.')

args = argparser.parse_args()

validate_forecast_args(args)

cls = parsers[args.parser]

parser = cls()
results = parser.run(args)

for result in results:
    print(results)
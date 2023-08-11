import requests
import pathlib
import json
import xml.etree.ElementTree as ET


HARDCODED_SITES = [
    "https://meta.stackoverflow.com",
]



def get_stackexchange_sites():
    feed = requests.get('https://stackexchange.com/feeds/sites').text
    root = ET.fromstring(feed)
    namespace = {'atom': 'http://www.w3.org/2005/Atom'}
    entry_ids = [entry.find('atom:id', namespace).text for entry in root.findall('atom:entry', namespace)]
    entry_ids.extend(HARDCODED_SITES)
    return [f"{site}/*" for site in sorted(entry_ids)]

def overwrite_manifest_json(sites: list[str]):
    manifest = json.loads(pathlib.Path('manifest.json').read_text())
    manifest['content_scripts'][0]['matches'] = sites
    pathlib.Path('manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == '__main__':
    sites = get_stackexchange_sites()
    overwrite_manifest_json(sites)
    print('Updated manifest.json')

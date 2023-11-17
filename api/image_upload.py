import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.uploader import upload

cloudinary.config(
  cloud_name = "dmusx7j1c",
  api_key = "365654555955232",
  api_secret = "KfVZ9P9IkwP0q_uAKwdfCqGAwoM"
)

def main():
  result = cloudinary.api.resource_by_asset_id("5ee181e1bfb60b1b649f3a615b5ea8f8")
  print(result)
  print(result['url'])

if __name__ == '__main__':
  main()
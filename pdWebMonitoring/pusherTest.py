import pusher

pusher_client = pusher.Pusher(
  app_id='573623',
  key='9c3b69d78c3088e46d6c',
  secret='5dd54a2e543746465100',
  cluster='us2',
  ssl=True
)


def main():
    pusher_client.trigger('temp-channel', 'temp-measure', {'message': "CALISS"})


if __name__ == "__main__":
    main()

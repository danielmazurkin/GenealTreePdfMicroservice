from config.base import Base, engine
import uvicorn
from api.v1.documents.download_pdf import app


def main():
    """Точка входа в микросервис."""
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
    uvicorn.run(app, host="0.0.0.0", port=8002)

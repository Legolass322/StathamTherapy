import uvicorn


def main():
    uvicorn.run("app.main:app", port=8080, log_level="info", reload=True)


if __name__ == "__main__":
    main()

import requests
import gc
#provides an interface to the python Garbage collector
#It provides features to enable collector, disable collector, tune collection frequency, debug options and more.
#garbage collector wil automatically clear the memory
#returned object count is greater, so there is a memory leak.

def call():
    # call the get with a url,here I used google.com
    # get method returns a response object
    response = requests.get('https://testing.zabehaty.uae.zabe7ti.website/api/regions)

    # print the status code of response
    print("Status code", response.status_code)

    # After the function is been returned,
    # the response object becomes non-referenced
    return


def main():
    print("No.of tracked objects before calling get method")

    # gc.get_objects() returns list objects been tracked
    # by the collector.
    # print the length of object list with len function.
    print(len(gc.get_objects()))

    # make a call to the function, that calls get method.
    call()

    # collect method immediately free the resource of
    # non-referenced object.
    gc.collect()

    # print the length of object list with len
    # function after removing non-referenced object.
    print("No.of tracked objects after removing non-referenced objects")
    print(len(gc.get_objects()))


if __name__ == "__main__":
    main()
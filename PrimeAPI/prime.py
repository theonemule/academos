from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_primes(max_value):
    primes = []
    for num in range(2, max_value + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

@app.route('/primes', methods=['GET'])
def get_primes():
    max_value = request.args.get('max', default=100, type=int)
    primes = calculate_primes(max_value)
    return jsonify(primes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
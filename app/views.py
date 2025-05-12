from django.shortcuts import render
import braintree
# Create your views here.

def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html",)

# Braintree configuration
# Make sure to replace these with your actual Braintree credentials     


# ✅ 直接在這裡填入測試用 Braintree 的金鑰（Sandbox 環境）
gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='os.getenv("MERCHANT_ID")',
    public_key='os.getenv("PUBLIC_KEY")',
    private_key='os.getenv("PRIVATE_KEY")',
  )
)

def payment(request):
    client_token = gateway.client_token.generate()
    return render(request, "app/payment.html", {"client_token": client_token})

def create_purchase():
    nonce_from_the_client = request.form["payment_method_nonce"]
    result = gateway.transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": request.POST["nonce"],
    })